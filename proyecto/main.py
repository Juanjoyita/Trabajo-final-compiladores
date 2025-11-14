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
            log.append(f.read() + "\n")  # Se abre el archivo.txt agrega contenido del archivo al log
    except:
        log.append("Error: No se pudo leer el archivo de entrada.\n")
        with open(output_text_file, "w") as f:
            f.write("\n".join(log))   # Guarda log parcial
        print(f"❌ Error al leer archivo. Revisa {output_text_file}")
        return

    # ================================
    # Análisis léxico (Lexer)
    # ================================
    input_stream = FileStream(input_file, encoding="utf-8")  # Crea stream para lexer
    lexer = LogicaLexer(input_stream)                        # Inicializa lexer

    lexer_errors = LexerErrorListener()  # Listener personalizado para errores léxicos
    lexer.removeErrorListeners()          # Elimina listeners por defecto
    lexer.addErrorListener(lexer_errors)  # Agrega listener personalizado

    tokens = CommonTokenStream(lexer)     # Genera stream de tokens
    tokens.fill()                         # Lee todos los tokens para detectar errores

    # Verifica errores léxicos
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
    # Análisis sintáctico (Parser)
    # ================================
    parser = LogicaParser(tokens)  # Inicializa parser con los tokens

    syntax_errors = SyntaxErrorListener()  # Listener para errores sintácticos
    parser.removeErrorListeners()           # Elimina listeners por defecto
    parser.addErrorListener(syntax_errors)  # Agrega listener personalizado

    tree = parser.program()  # Construye árbol de parseo (AST)

    # Verifica errores sintácticos
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
    # Análisis semántico
    # ================================
    analyzer = SemanticAnalyzer()  # Inicializa analizador semántico
    semantic_ok = analyzer.visit(tree)  # Recorre AST para validar tipos y variables

    # Verifica errores semánticos
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
    generator = CodeGenerator()           # Inicializa generador de código
    output_program = generator.visit(tree)  # Genera código Python desde AST

    with open(output_program_file, "w") as f:
        f.write(output_program)           # Guarda código generado

    log.append(f"[CODEGEN]\n✔ Código generado en {output_program_file}.\n")

    # ================================
    # Ejecutar programa generado
    # ================================
    log.append("[PYTHON OUTPUT]\n")

    try:
        result = subprocess.run(
            ["python3", output_program_file],  # Ejecuta el archivo Python
            capture_output=True,               # Captura salida estándar
            text=True
        )
        log.append(result.stdout.strip() + "\n")  # Agrega salida al log
    except Exception as e:
        log.append(f"Error al ejecutar el programa generado: {e}\n")

    log.append("[EJECUCIÓN COMPLETADA]\n")

    # ================================
    # Guardar log final
    # ================================
    with open(output_text_file, "w") as f:
        f.write("\n".join(log))  # Guarda todo el registro de ejecución

    print(f"✅ Test finalizado. Revisa {output_text_file} y {output_program_file}")


# Punto de entrada del script
if __name__ == "__main__":
    main()
