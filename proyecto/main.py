import sys
import subprocess
from antlr4 import *
import os

from generated.LogicaLexer import LogicaLexer
from generated.LogicaParser import LogicaParser

from semantic_analyzer.semantic_visitor import SemanticAnalyzer
from semantic_analyzer.listener import LexerErrorListener, SyntaxErrorListener
from codegen.generator import CodeGenerator


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

    # =========================================
    #   LEER INPUT
    # =========================================
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
    #   LÉXICO (LEXER)
    # =========================================
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = LogicaLexer(input_stream)

    # ✅ MANEJADOR DE ERRORES LÉXICOS
    lexer_errors = LexerErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_errors)

    tokens = CommonTokenStream(lexer)
    tokens.fill()   # IMPORTANTE: obliga a leer todos los tokens y detectar errores

    # ✅ DETECTAR ERRORES LÉXICOS
    if lexer_errors.errors:
        log.append("[LÉXICOS]\n")
        for e in lexer_errors.errors:
            log.append("  - " + e)
        log.append("\n[ESTADO] ❌ Compilación fallida por errores léxicos.\n")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))

        print(f"❌ Errores léxicos. Revisa {output_text_file}")
        return

    # =========================================
    #   SINTAXIS (PARSER)
    # =========================================
    parser = LogicaParser(tokens)

    # ✅ MANEJADOR DE ERRORES SINTÁCTICOS
    syntax_errors = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(syntax_errors)

    tree = parser.program()

    # ✅ DETECTAR ERRORES SINTÁCTICOS
    if syntax_errors.errors:
        log.append("[SINTÁCTICOS]\n")
        for e in syntax_errors.errors:
            log.append("  - " + e)

        log.append("\n[ESTADO] ❌ Compilación fallida por errores sintácticos.\n")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))

        print(f"❌ Errores sintácticos. Revisa {output_text_file}")
        return

    # =========================================
    #   ANÁLISIS SEMÁNTICO
    # =========================================
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

    # =========================================
    #   GENERACIÓN DE CÓDIGO SOLO SI TODO ESTÁ BIEN
    # =========================================
    generator = CodeGenerator()
    output_program = generator.visit(tree)

    with open(output_program_file, "w") as f:
        f.write(output_program)

    log.append(f"[CODEGEN]\n✔ Código generado en {output_program_file}.\n")

    # =========================================
    #   EJECUTAR PROGRAMA GENERADO
    # =========================================
    log.append("[PYTHON OUTPUT]\n")

    try:
        result = subprocess.run(
            ["python3", output_program_file],
            capture_output=True,
            text=True
        )
        log.append(result.stdout.strip() + "\n")
    except Exception as e:
        log.append(f"Error al ejecutar el programa generado: {e}")

    log.append("[EJECUCIÓN COMPLETADA]\n")

    # =========================================
    #   GUARDAR LOG FINAL
    # =========================================
    with open(output_text_file, "w") as f:
        f.write("\n".join(log))

    print(f"✅ Test finalizado. Revisa {output_text_file} y {output_program_file}")


if __name__ == "__main__":
    main()