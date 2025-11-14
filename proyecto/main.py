import sys
import subprocess
from antlr4 import *
import os

from generated.LogicaLexer import LogicaLexer
from generated.LogicaParser import LogicaParser

from semantic_analyzer.semantic_visitor import SemanticAnalyzer
from semantic_analyzer.listener import LexerErrorListener, SyntaxErrorListener

from codegen.generator import CodeGenerator


# ======================================================
# FUNCIÓN PARA IMPRIMIR ÁRBOL SINTÁCTICO JERÁRQUICO
# ======================================================
def print_tree(node, rule_names, indent=""):
    if node.getChildCount() == 0:
        print(indent + f"- {node.getText()}")
        return

    rule_name = rule_names[node.getRuleIndex()]
    print(indent + f"[{rule_name}]")

    for i in range(node.getChildCount()):
        print_tree(node.getChild(i), rule_names, indent + "  ")


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py input.txt")
        return

    input_file = sys.argv[1]

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_text_file = f"output_{base_name}.txt"
    output_program_file = f"output_program_{base_name}.py"

    log = []
    log.append("===== Mini Compilador - Registro de Ejecución =====\n")

    # ================================
    # Leer archivo de entrada
    # ================================
    log.append("[INPUT]\n")
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            log.append(f.read() + "\n")
    except:
        log.append("Error: No se pudo leer el archivo de entrada.\n")
        with open(output_text_file, "w") as f:
            f.write("\n".join(log))
        print(f"❌ Error al leer archivo. Revisa {output_text_file}")
        return

    # ================================
    # FASE LÉXICA
    # ================================
    print(">>> INICIANDO FASE LÉXICA...")
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = LogicaLexer(input_stream)

    lexer_errors = LexerErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_errors)

    tokens = CommonTokenStream(lexer)
    tokens.fill()

    if lexer_errors.errors:
        log.append("[LÉXICO]\n")
        for e in lexer_errors.errors:
            log.append("  - " + e)
        log.append("\n[ESTADO] ❌ Compilación fallida por errores léxicos.\n")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))

        print("❌ Se encontraron errores léxicos.")
        return

    print("✔ [LÉXICO] Fase completada sin errores.")
    log.append("[LÉXICO]\n✔ Fase completada sin errores.\n")

    # ================================
    # FASE SINTÁCTICA
    # ================================
    print(">>> INICIANDO FASE SINTÁCTICA...")
    parser = LogicaParser(tokens)

    syntax_errors = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(syntax_errors)

    tree = parser.program()

    if syntax_errors.errors:
        log.append("[SINTÁCTICOS]\n")
        for e in syntax_errors.errors:
            log.append("  - " + e)
        log.append("\n[ESTADO] ❌ Compilación fallida por errores sintácticos.\n")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))

        print("❌ Se encontraron errores sintácticos.")
        return

    print("✔ [SINTAXIS] Árbol sintáctico construido correctamente.\n")
    log.append("[SINTAXIS]\n✔ Árbol sintáctico construido correctamente.\n")

    # Mostrar árboles
    print("\n============== ÁRBOL SINTÁCTICO (LISP) =============\n")
    print(tree.toStringTree(recog=parser))
    print("\n=========== ÁRBOL SINTÁCTICO (JERÁRQUICO) =========\n")
    print_tree(tree, parser.ruleNames)
    print("\n===================================================\n")

    # ================================
    # FASE SEMÁNTICA
    # ================================
    print(">>> INICIANDO FASE SEMÁNTICA...")
    analyzer = SemanticAnalyzer()
    semantic_ok = analyzer.visit(tree)

    if analyzer.errors:
        log.append("[SEMÁNTICA]\n")
        for e in analyzer.errors:
            log.append("  - " + e)
        log.append("\n[ESTADO] ❌ Compilación fallida por errores semánticos.\n")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))

        print("❌ Se encontraron errores semánticos.")
        return

    print("✔ [SEMÁNTICA] Análisis semántico completado.")
    log.append("[SEMÁNTICA]\n✔ Sin errores semánticos.\n")

    # ================================
    # GENERACIÓN DE CÓDIGO
    # ================================
    print(">>> GENERANDO CÓDIGO PYTHON...")
    generator = CodeGenerator()
    output_program = generator.visit(tree)

    with open(output_program_file, "w") as f:
        f.write(output_program)

    print("✔ [CODEGEN] Código Python generado exitosamente.")
    log.append("[CODEGEN]\n✔ Código Python generado exitosamente.\n")

    # ================================
    # EJECUCIÓN DEL PROGRAMA
    # ================================
    print(">>> EJECUTANDO PROGRAMA GENERADO...")
    log.append("[PYTHON OUTPUT]\n")

    try:
        result = subprocess.run(
            ["python3", output_program_file],
            capture_output=True,
            text=True
        )
        print("Salida del programa:")
        print(result.stdout.strip())
        log.append(result.stdout.strip() + "\n")
    except Exception as e:
        error_msg = f"Error al ejecutar el programa generado: {e}"
        print(error_msg)
        log.append(error_msg + "\n")

    print("\n✔ [EJECUCIÓN] Programa ejecutado correctamente.\n")
    log.append("✔ [EJECUCIÓN] Programa ejecutado correctamente.\n")

    log.append("[EJECUCIÓN COMPLETADA]\n")

    with open(output_text_file, "w") as f:
        f.write("\n".join(log))

    print(f"✅ Test finalizado. Revisa {output_text_file} y {output_program_file}")


if __name__ == "__main__":
    main()
