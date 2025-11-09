import sys
import subprocess
from antlr4 import *

from generated.LogicaLexer import LogicaLexer
from generated.LogicaParser import LogicaParser

from semantic_analyzer.semantic_visitor import SemanticAnalyzer
from codegen.generator import CodeGenerator
import os


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py input.txt")
        return

    input_file = sys.argv[1]

    # =========================================
    #   NOMBRE BASE PARA ARCHIVOS DE SALIDA
    # =========================================
    base_name = os.path.splitext(os.path.basename(input_file))[0]

    output_text_file = f"output_{base_name}.txt"
    output_program_file = f"output_program_{base_name}.py"

    log = []
    log.append("===== Mini Compilador - Registro de Ejecución =====\n")

    # Leer INPUT
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

    # =========================================
    #   LEXER + PARSER
    # =========================================
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = LogicaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = LogicaParser(tokens)

    tree = parser.program()

    # =========================================
    #   ANÁLISIS SEMÁNTICO
    # =========================================
    analyzer = SemanticAnalyzer()
    semantic_ok = analyzer.visit(tree)

    if analyzer.errors:
        log.append("[SEMÁNTICA]\n")
        for e in analyzer.errors:
            log.append("  - " + e)
        log.append(f"\n[ESTADO] ❌ Compilación fallida.\n")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))

        print(f"❌ Errores semánticos. Revisa {output_text_file}")
        return

    log.append("[SEMÁNTICA]\n✔ Sin errores semánticos.\n")

    # =========================================
    #   GENERACIÓN DE CÓDIGO
    # =========================================
    generator = CodeGenerator()
    output_program = generator.visit(tree)

    with open(output_program_file, "w") as f:
        f.write(output_program)

    log.append(f"[CODEGEN]\n✔ Código generado en {output_program_file}.\n")

    # =========================================
    #   EJECUCIÓN DEL PROGRAMA GENERADO
    # =========================================
    log.append("[PYTHON OUTPUT]\n")

    try:
        result = subprocess.run(
            ["python3", output_program_file],
            capture_output=True,
            text=True
        )
        log.append(result.stdout)
    except Exception as e:
        log.append(f"Error al ejecutar el programa generado: {e}")

    log.append("\n[EJECUCIÓN COMPLETADA]\n")

    # =========================================
    #   GUARDAR OUTPUT FINAL
    # =========================================
    with open(output_text_file, "w") as f:
        f.write("\n".join(log))

    print(f"✅ Test finalizado. Revisa {output_text_file} y {output_program_file}")


if __name__ == "__main__":
    main()
