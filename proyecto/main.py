import sys                   # Permite leer argumentos desde la terminal, por ejemplo: python main.py input.txt
import subprocess            # Permite ejecutar el programa Python que el compilador genera al final
from antlr4 import *         # Importa todas las clases necesarias para usar ANTLR en Python (Lexer, Parser, ParseTree)
import os                    # Manejo de rutas de archivos, nombres y extensiones

# Importación del Lexer y Parser generados automáticamente por ANTLR
from generated.LogicaLexer import LogicaLexer      # Analizador léxico: convierte caracteres → tokens
from generated.LogicaParser import LogicaParser    # Analizador sintáctico: convierte tokens → árbol sintáctico (AST)

# Importación de los listeners personalizados para manejo de errores léxicos y sintácticos
from semantic_analyzer.semantic_visitor import SemanticAnalyzer     # Visitante que analiza errores semánticos
from semantic_analyzer.listener import LexerErrorListener, SyntaxErrorListener  # Detectan errores en tiempo de compilación

# Generador de código Python final (código ejecutable traducido del lenguaje lógico)
from codegen.generator import CodeGenerator

# Generador de código intermedio IR / TAC (Three Address Code)
from codegen.ir_generator import IRGenerator


# ======================================================
# FUNCIÓN PARA IMPRIMIR EL ÁRBOL SINTÁCTICO
# ======================================================
def print_tree(node, rule_names, indent=""):
    """
    Imprime el árbol AST con indentación para visualizar la estructura del programa.
    Esto es útil para entender cómo el parser interpreta el código fuente.
    """
    if node.getChildCount() == 0:          # Si es un nodo hoja (token final)
        print(indent + f"- {node.getText()}")
        return

    rule_name = rule_names[node.getRuleIndex()]    # Obtiene el nombre de la regla
    print(indent + f"[{rule_name}]")

    # Procesa hijos del nodo recursivamente
    for i in range(node.getChildCount()):
        print_tree(node.getChild(i), rule_names, indent + "  ")


# ======================================================
# MAIN PRINCIPAL DEL COMPILADOR
# ======================================================
def main():

    # Verifica que se haya pasado un archivo como argumento
    if len(sys.argv) < 2:
        print("Uso: python main.py input.txt")
        return

    input_file = sys.argv[1]  # Archivo que contiene el código fuente del usuario

    # Construye nombres automáticos para los archivos de salida
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_text_file = f"output_{base_name}.txt"             # Archivo de LOG
    output_program_file = f"output_program_{base_name}.py"   # Código Python generado

    log = []   # Lista para almacenar todo el registro del proceso
    log.append("===== Mini Compilador - Registro de Ejecución =====\n")

    # ======================================================
    # 1. FASE DE LECTURA DEL FUENTE
    # ======================================================
    log.append("[INPUT]\n")
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            log.append(f.read() + "\n")    # Guarda el contenido del archivo en el log
    except:
        log.append("Error: No se pudo leer el archivo.\n")
        with open(output_text_file, "w") as f:
            f.write("\n".join(log))
        return

    # ======================================================
    # 2. FASE LÉXICA — LEXER
    # ======================================================
    print(">>> FASE LÉXICA...")

    input_stream = FileStream(input_file, encoding="utf-8")  # Carga el archivo como flujo de caracteres
    lexer = LogicaLexer(input_stream)                        # Crea el lexer sobre el flujo

    # Se instalan los listeners de error personalizados
    lexer_errors = LexerErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_errors)

    tokens = CommonTokenStream(lexer)   # Convierte los tokens encontrados a un buffer
    tokens.fill()                        # Fuerza a que el lexer procese toda la entrada

    if lexer_errors.errors:             # Si hubo errores léxicos, se detiene el proceso
        log.append("[LÉXICOS]\n")
        for e in lexer_errors.errors:
            log.append("  - " + e)
        print("❌ Error léxico.")
        return

    print("✔ Léxico OK")
    log.append("[LÉXICOS] ✔ Sin errores\n")

    # ======================================================
    # 3. FASE SINTÁCTICA — PARSER
    # ======================================================
    print(">>> FASE SINTÁCTICA...")

    parser = LogicaParser(tokens)       # Crea el parser usando los tokens detectados

    syntax_errors = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(syntax_errors)

    tree = parser.program()             # Punto inicial del lenguaje (regla raíz)

    if syntax_errors.errors:            # Si hubo errores en la estructura del lenguaje
        log.append("[SINTÁCTICOS]\n")
        for e in syntax_errors.errors:
            log.append("  - " + e)
        print("❌ Error sintáctico.")
        return

    print("✔ Sintaxis OK")
    log.append("[SINTÁCTICOS] ✔ Sin errores\n")

    # ======================================================
    # 4. FASE SEMÁNTICA — VALIDACIÓN DE SIGNIFICADO
    # ======================================================
    print(">>> FASE SEMÁNTICA...")

    analyzer = SemanticAnalyzer()   # Analizador semántico creado por ti
    analyzer.visit(tree)            # Recorre el AST y valida reglas semánticas

    if analyzer.errors:
        log.append("[SEMÁNTICA]\n")
        for e in analyzer.errors:
            log.append("  - " + e)
        print("❌ Error semántico.")
        return

    print("✔ Semántica OK")
    log.append("[SEMÁNTICA] ✔ Sin errores\n")

    # ======================================================
    # 5. GENERACIÓN DE IR (Intermediate Representation / TAC)
    # ======================================================
    print(">>> GENERANDO IR (Intermediate Representation)...")

    ir_generator = IRGenerator()       # Instancia del generador de IR
    ir_code = ir_generator.visit(tree) # Recorre el AST y devuelve lista de instrucciones TAC

    print("✔ IR generado correctamente.\n")
    print("=== CÓDIGO IR ===")
    for instr in ir_code:
        print(instr)

    log.append("[IR] ✔ IR generado\n")
    for instr in ir_code:
        log.append("  " + instr)

    # ======================================================
    # 6. GENERACIÓN DE CÓDIGO PYTHON – CODEGEN
    # ======================================================
    print(">>> GENERANDO CÓDIGO PYTHON...")

    generator = CodeGenerator()          # Genera un archivo Python ejecutable
    output_program = generator.visit(tree)

    with open(output_program_file, "w") as f:
        f.write(output_program)

    print("✔ CODEGEN OK")
    log.append("[CODEGEN] ✔ Python generado\n")

    # ======================================================
    # 7. EJECUCIÓN DEL PROGRAMA PYTHON GENERADO
    # ======================================================
    print(">>> EJECUTANDO PROGRAMA...")

    log.append("[PYTHON OUTPUT]\n")

    try:
        # Ejecuta el archivo Python generado y captura su salida
        result = subprocess.run(
            ["python3", output_program_file],
            capture_output=True,
            text=True
        )
        print(result.stdout)      # Muestra en consola
        log.append(result.stdout) # Guarda en el log
    except Exception as e:
        print("❌ Error al ejecutar:", e)
        log.append(str(e))

    # ======================================================
    # 8. GUARDADO DEL LOG FINAL
    # ======================================================
    log.append("[FIN DEL PROCESO]\n")
    with open(output_text_file, "w") as f:
        f.write("\n".join(log))

    print(f"✔ Proceso completado. Revisa {output_text_file} y {output_program_file}")


# Punto de entrada estándar de Python
if __name__ == "__main__":
    main()
