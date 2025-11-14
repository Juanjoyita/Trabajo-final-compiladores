import sys            # Permite acceder a argumentos de línea de comando
import subprocess     # Permite ejecutar comandos externos (aquí, Python)
from antlr4 import *  # Librería ANTLR para lexer/parser
import os             # Operaciones de sistema (archivos y rutas)

# Importa lexer y parser generados por ANTLR
from generated.LogicaLexer import LogicaLexer
from generated.LogicaParser import LogicaParser

# Importa analizador semántico y listeners de errores
from semantic_analyzer.semantic_visitor import SemanticAnalyzer
from semantic_analyzer.listener import LexerErrorListener, SyntaxErrorListener

# Importa generador de código Python
from codegen.generator import CodeGenerator


# ======================================================
# FUNCIÓN PARA IMPRIMIR ÁRBOL SINTÁCTICO JERÁRQUICO
# ======================================================
def print_tree(node, rule_names, indent=""):
    """
    Imprime el árbol sintáctico en formato jerárquico.
    """
    if node.getChildCount() == 0:
        print(indent + f"- {node.getText()}")
        return

    rule_name = rule_names[node.getRuleIndex()]
    print(indent + f"[{rule_name}]")

    for i in range(node.getChildCount()):
        print_tree(node.getChild(i), rule_names, indent + "  ")


def main():
    # Verifica que se haya pasado un archivo de entrada
    if len(sys.argv) < 2:
        print("Uso: python main.py input.txt")
        return

    input_file = sys.argv[1]  # Archivo de entrada proporcionado por el usuario

    # ================================
    # Definir nombres de archivos de salida
    # ================================
    base_name = os.path.splitext(os.path.basename(input_file))[0]  # Nombre de los archivos de salida 
    output_text_file = f"output_{base_name}.txt"          # Archivo registro de compilación
    output_program_file = f"output_program_{base_name}.py"  # Archivo Python generado

    # Inicializa el registro de ejecución
    log = []
    log.append("===== Mini Compilador - Registro de Ejecución =====\n")

    # ================================
    # Leer contenido del archivo de entrada
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
    # Análisis léxico
    # ================================
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = LogicaLexer(input_stream)

    lexer_errors = LexerErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_errors)

    tokens = CommonTokenStream(lexer)
    tokens.fill()

    if lexer_errors.errors:
        log.append("[LÉXICOS]\n")
        for e in lexer_errors.errors:
            log.append("  - " + e)
        log.append("\n[ESTADO] ❌ Compilación fallida por errores léxicos.\n")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))
        print(f"❌ Errores léxicos. Revisa {output_text_file}")
        return

    # ================================
    # Análisis sintáctico
    # ================================
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
        print(f"❌ Errores sintácticos. Revisa {output_text_file}")
        return

    # ================================
    # MOSTRAR ÁRBOLES SINTÁCTICOS (SOLO EN TESTS VÁLIDOS)
    # ================================
    print("\n===================================================")
    print("============== ÁRBOL SINTÁCTICO (LISP) =============")
    print("===================================================\n")
    print(tree.toStringTree(recog=parser))
    print("\n===================================================")
    print("=========== ÁRBOL SINTÁCTICO (JERÁRQUICO) =========")
    print("===================================================\n")
    print_tree(tree, parser.ruleNames)
    print("\n===================================================\n")

    # ================================
    # Análisis semántico
    # ================================
    analyzer = SemanticAnalyzer()
    semantic_ok = analyzer.visit(tree)

    if analyzer.errors:
        log.append("[SEMÁNTICA]\n")
        for e in analyzer.errors:
            log.append("  - " + e)
        log.append("\n[ESTADO] ❌ Compilación fallida por errores semánticos.\n")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))

        print(f"❌ Errores semánticos. Revisa {output_text_file}")
        return

    log.append("[SEMÁNTICA]\n✔ Sin errores semánticos.\n")

    # ================================
    # Generación de código Python
    # ================================
    generator = CodeGenerator()
    output_program = generator.visit(tree)

    with open(output_program_file, "w") as f:
        f.write(output_program)

    log.append(f"[CODEGEN]\n✔ Código generado en {output_program_file}.\n")

    # ================================
    # Ejecutar el programa generado
    # ================================
    log.append("[PYTHON OUTPUT]\n")

    try:
        result = subprocess.run(
            ["python3", output_program_file],
            capture_output=True,
            text=True
        )
        log.append(result.stdout.strip() + "\n")
    except Exception as e:
        log.append(f"Error al ejecutar el programa generado: {e}\n")

    log.append("[EJECUCIÓN COMPLETADA]\n")

    with open(output_text_file, "w") as f:
        f.write("\n".join(log))

    print(f"✅ Test finalizado. Revisa {output_text_file} y {output_program_file}")


if __name__ == "__main__":
    main()
