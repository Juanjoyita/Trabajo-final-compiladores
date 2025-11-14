import sys
import subprocess
from antlr4 import *
import os

# Importación del lexer y parser generados por ANTLR
from generated.LogicaLexer import LogicaLexer
from generated.LogicaParser import LogicaParser

# Listeners personalizados para errores y el analizador semántico
from semantic_analyzer.semantic_visitor import SemanticAnalyzer
from semantic_analyzer.listener import LexerErrorListener, SyntaxErrorListener

# Generador de código Python a partir del AST
from codegen.generator import CodeGenerator


# ======================================================
# FUNCIÓN PARA IMPRIMIR EL ÁRBOL SINTÁCTICO JERÁRQUICO
# ======================================================
def print_tree(node, rule_names, indent=""):
    """
    Recorre de forma recursiva el árbol sintáctico y lo imprime
    con identación para visualizar su estructura jerárquica.
    """
    # Si el nodo NO tiene hijos, es un token terminal
    if node.getChildCount() == 0:
        print(indent + f"- {node.getText()}")
        return

    # Si tiene hijos, es una regla de la gramática
    rule_name = rule_names[node.getRuleIndex()]
    print(indent + f"[{rule_name}]")

    # Recorre los hijos aumentando la indentación
    for i in range(node.getChildCount()):
        print_tree(node.getChild(i), rule_names, indent + "  ")


# ======================================================
# MAIN PRINCIPAL DEL COMPILADOR
# ======================================================
def main():

    # -------------------------------------
    # Verificar archivo ingresado en consola
    # -------------------------------------
    if len(sys.argv) < 2:
        print("Uso: python main.py input.txt")
        return

    input_file = sys.argv[1]

    # Crear nombres de archivos de salida (log y código generado)
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_text_file = f"output_{base_name}.txt"
    output_program_file = f"output_program_{base_name}.py"

    # Archivo log del proceso de compilación
    log = []
    log.append("===== Mini Compilador - Registro de Ejecución =====\n")

    # ======================================================
    # 1. LECTURA DEL ARCHIVO FUENTE
    # ======================================================
    log.append("[INPUT]\n")
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            log.append(f.read() + "\n")
    except:
        log.append("Error: No se pudo leer el archivo.\n")
        with open(output_text_file, "w") as f:
            f.write("\n".join(log))
        print(f"❌ Error al leer archivo. Revisa {output_text_file}")
        return

    # ======================================================
    # 2. FASE LÉXICA
    # ======================================================
    print(">>> INICIANDO FASE LÉXICA...")

    # Crear flujo de entrada para el lexer
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = LogicaLexer(input_stream)

    # Agregar listener personalizado para capturar errores léxicos
    lexer_errors = LexerErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_errors)

    # Generar la lista de tokens
    tokens = CommonTokenStream(lexer)
    tokens.fill()

    # Si hubo errores léxicos, detener compilación
    if lexer_errors.errors:
        log.append("[LÉXICOS]\n")
        for e in lexer_errors.errors:
            log.append("  - " + e)
        log.append("\n[ESTADO] ❌ Compilación fallida por errores léxicos.\n")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))

        print("❌ Se encontraron errores léxicos.")
        return

    print("✔ [LÉXICO] Fase completada sin errores.")
    log.append("[LÉXICOS]\n✔ Sin errores léxicos.\n")

    # ======================================================
    # 3. FASE SINTÁCTICA
    # ======================================================
    print(">>> INICIANDO FASE SINTÁCTICA...")

    parser = LogicaParser(tokens)

    # Listener personalizado para errores sintácticos
    syntax_errors = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(syntax_errors)

    # Generar árbol sintáctico
    tree = parser.program()

    # Si hay errores de sintaxis, detener compilación
    if syntax_errors.errors:
        log.append("[SINTÁCTICOS]\n")
        for e in syntax_errors.errors:
            log.append("  - " + e)
        log.append("\n[ESTADO] ❌ Compilación fallida por errores sintácticos.\n")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))

        print("❌ Se encontraron errores sintácticos.")
        return

    print("✔ [SINTAXIS] Árbol sintáctico construido correctamente.")
    log.append("[SINTÁCTICOS]\n✔ Sin errores sintácticos.\n")

    # ======================================================
    # 4. FASE SEMÁNTICA
    # ======================================================
    print(">>> INICIANDO FASE SEMÁNTICA...")

    analyzer = SemanticAnalyzer()
    semantic_ok = analyzer.visit(tree)

    # Si hay errores semánticos, detener
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

    # ======================================================
    # 5. MOSTRAR ÁRBOLES (solo si no hubo errores)
    # ======================================================
    print("\n============== ÁRBOL SINTÁCTICO (LISP) =============\n")
    print(tree.toStringTree(recog=parser))

    print("\n=========== ÁRBOL SINTÁCTICO (JERÁRQUICO) =========\n")
    print_tree(tree, parser.ruleNames)
    print("\n===================================================\n")

    # ======================================================
    # 6. GENERACIÓN DE CÓDIGO
    # ======================================================
    print(">>> GENERANDO CÓDIGO PYTHON...")

    generator = CodeGenerator()
    output_program = generator.visit(tree)

    # Guardar archivo Python generado
    with open(output_program_file, "w") as f:
        f.write(output_program)

    print("✔ [CODEGEN] Código Python generado exitosamente.")
    log.append(f"[CODEGEN]\n✔ Código generado en {output_program_file}.\n")

    # ======================================================
    # 7. EJECUTAR EL CÓDIGO PYTHON GENERADO
    # ======================================================
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

        print("\n✔ [EJECUCIÓN] Programa ejecutado correctamente.\n")

    except Exception as e:
        error_msg = f"Error al ejecutar el programa generado: {e}\n"
        print(error_msg)
        log.append(error_msg)

    log.append("[EJECUCIÓN COMPLETADA]\n")

    # ======================================================
    # 8. GUARDAR EL LOG FINAL
    # ======================================================
    with open(output_text_file, "w") as f:
        f.write("\n".join(log))

    print(f"✅ Test finalizado. Revisa {output_text_file} y {output_program_file}")


# Entrada principal del programa
if __name__ == "__main__":
    main()
