import sys
import subprocess
from antlr4 import *

from generated.LogicaLexer import LogicaLexer
from generated.LogicaParser import LogicaParser

from semantic_analyzer.semantic_visitor import SemanticAnalyzer
from codegen.generator import CodeGenerator


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py input.txt")
        return

    input_file = sys.argv[1]

    # ============================
    #   Abrir archivo output.txt
    # ============================
    log = []
    log.append("===== Mini Compilador - Registro de Ejecución =====\n")

    # Leer INPUT
    log.append("[INPUT]\n")
    try:
        with open(input_file, "r") as f:
            log.append(f.read() + "\n")
    except:
        log.append("Error: No se pudo leer el archivo de entrada.\n")
        with open("output.txt", "w") as f:
            f.write("\n".join(log))
        return

    # ============================
    #   LEXER + PARSER
    # ============================
    input_stream = FileStream(input_file)
    lexer = LogicaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = LogicaParser(tokens)

    tree = parser.program()

    # ============================
    #   ANALISIS SEMÁNTICO
    # ============================
    analyzer = SemanticAnalyzer()
    semantic_ok = analyzer.visit(tree)

    if analyzer.errors:
        log.append("[SEMÁNTICA]\n")
        for e in analyzer.errors:
            log.append("  - " + e)
        log.append("\n[ESTADO] ❌ Compilación fallida.\n")

        with open("output.txt", "w") as f:
            f.write("\n".join(log))

        print("❌ Errores semánticos detectados. Revisa output.txt.")
        return

    log.append("[SEMÁNTICA]\n✔ Sin errores semánticos.\n")

    # ============================
    #   GENERACIÓN DE CÓDIGO
    # ============================
    generator = CodeGenerator()
    output_program = generator.visit(tree)

    with open("output_program.py", "w") as f:
        f.write(output_program)

    log.append("[CODEGEN]\n✔ Código generado en output_program.py.\n")

    # ============================
    #   EJECUCIÓN DEL PROGRAMA GENERADO
    # ============================
    log.append("[PYTHON OUTPUT]\n")

    try:
        result = subprocess.run(
            ["python3", "output_program.py"],
            capture_output=True,
            text=True
        )
        log.append(result.stdout)
    except Exception as e:
        log.append(f"Error al ejecutar el programa generado: {e}")

    log.append("\n[EJECUCIÓN COMPLETADA]\n")

    # ============================
    #   GUARDAR OUTPUT FINAL
    # ============================
    with open("output.txt", "w") as f:
        f.write("\n".join(log))

    print("✅ Todo OK. Revisa output.txt y output_program.py")


if __name__ == "__main__":
    main()
