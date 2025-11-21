import sys                   # Permite leer argumentos desde la terminal (por ej. input.txt)
import subprocess            # Se usa para ejecutar el archivo Python generado por el compilador
from antlr4 import *         # Librerías base de ANTLR para crear lexer, parser y recorrer el árbol
import os                    # Manejo de rutas de archivos en el sistema operativo

# Importación del Lexer y Parser generados automáticamente por ANTLR
from generated.LogicaLexer import LogicaLexer
from generated.LogicaParser import LogicaParser

# Importamos los listeners personalizados para errores léxicos/sintácticos
from semantic_analyzer.semantic_visitor import SemanticAnalyzer
from semantic_analyzer.listener import LexerErrorListener, SyntaxErrorListener

# Importamos generador de código Python final
from codegen.generator import CodeGenerator

# Importamos generador del IR (Intermediate Representation / Código de 3 direcciones)
from codegen.ir_generator import IRGenerator


# ======================================================
# FUNCIÓN PARA IMPRIMIR EL ÁRBOL SINTÁCTICO
# ======================================================
def print_tree(node, rule_names, indent=""):
    """
    Imprime el árbol sintáctico con indentación visual.
    Esto se usa solo como herramienta de depuración.
    """
    # Nodo terminal → token literal
    if node.getChildCount() == 0:
        print(indent + f"- {node.getText()}")
        return

    # Nodo compuesto → regla de la gramática
    rule_name = rule_names[node.getRuleIndex()]
    print(indent + f"[{rule_name}]")

    # Recorrer hijos recursivamente
    for i in range(node.getChildCount()):
        print_tree(node.getChild(i), rule_names, indent + "  ")


# ======================================================
# MAIN PRINCIPAL DEL COMPILADOR
# ======================================================
def main():

    # ----------------------------------------------------
    # 0. Verificar archivo de entrada
    # ----------------------------------------------------
    if len(sys.argv) < 2:
        print("Uso: python main.py input.txt")
        return

    input_file = sys.argv[1]  # Ruta del archivo fuente a compilar

    # Construimos nombres para los archivos de salida
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_text_file = f"output_{base_name}.txt"            # Archivo log
    output_program_file = f"output_program_{base_name}.py"  # Código Python generado

    log = []  # Lista para registrar todo lo que pasa en el compilador
    log.append("===== Mini Compilador - Registro de Ejecución =====\n")

    # ======================================================
    # 1. LECTURA DEL ARCHIVO DE ENTRADA
    # ======================================================
    log.append("[INPUT]\n")
    try:
        # Intentamos leer el archivo fuente
        with open(input_file, "r", encoding="utf-8") as f:
            log.append(f.read() + "\n")
    except:
        # Si falla → igual guardamos log
        log.append("Error: No se pudo leer el archivo.\n")
        with open(output_text_file, "w") as f:
            f.write("\n".join(log))
        return

    # ======================================================
    # 2. FASE LÉXICA
    # ======================================================
    print(">>> FASE LÉXICA...")

    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = LogicaLexer(input_stream)

    # Listener personalizado para errores léxicos
    lexer_errors = LexerErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_errors)

    # Convertimos tokens en flujo para el parser
    tokens = CommonTokenStream(lexer)
    tokens.fill()

    # Si hay errores léxicos → detener compilación pero guardar log
    if lexer_errors.errors:
        log.append("[LÉXICOS]\n")
        for e in lexer_errors.errors:
            log.append("  - " + e)

        print("❌ Error léxico.")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))
        return

    print("✔ Léxico OK")
    log.append("[LÉXICOS] ✔ Sin errores\n")

    # ======================================================
    # 3. FASE SINTÁCTICA
    # ======================================================
    print(">>> FASE SINTÁCTICA...")

    parser = LogicaParser(tokens)

    # Listener personalizado de errores sintácticos
    syntax_errors = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(syntax_errors)

    # Parseamos el programa completo
    tree = parser.program()

    # Si hubo errores sintácticos → detener compilación pero guardar log
    if syntax_errors.errors:
        log.append("[SINTÁCTICOS]\n")
        for e in syntax_errors.errors:
            log.append("  - " + e)

        print("❌ Error sintáctico.")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))
        return

    print("✔ Sintaxis OK")
    log.append("[SINTÁCTICOS] ✔ Sin errores\n")

    # ======================================================
    # 4. FASE SEMÁNTICA
    # ======================================================
    print(">>> FASE SEMÁNTICA...")

    analyzer = SemanticAnalyzer()  # Comprobador semántico
    analyzer.visit(tree)

    # Si hay errores semánticos → guardar log y detener
    if analyzer.errors:
        log.append("[SEMÁNTICA]\n")
        for e in analyzer.errors:
            log.append("  - " + e)

        print("❌ Error semántico.")

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))
        return

    print("✔ Semántica OK")
    log.append("[SEMÁNTICA] ✔ Sin errores\n")

    # ======================================================
    # 5. FASE DE IR (INTERMEDIATE REPRESENTATION)
    # ======================================================
    print(">>> GENERANDO IR...")

    try:
        ir_generator = IRGenerator()   # Generador TAC
        ir_code = ir_generator.visit(tree)

        print("✔ IR generado correctamente.\n")
        print("=== CÓDIGO IR ===")
        for instr in ir_code:
            print(instr)

        log.append("[IR] ✔ IR generado\n")
        for instr in ir_code:
            log.append("  " + instr)

    except Exception as e:
        # Si falla el IR → registrar error y salir
        print("❌ Error generando IR:", e)
        log.append("[IR] Error: " + str(e))

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))
        return

    # ======================================================
    # 6. GENERACIÓN DEL CÓDIGO PYTHON FINAL
    # ======================================================
    print(">>> GENERANDO CÓDIGO PYTHON...")

    try:
        generator = CodeGenerator()
        output_program = generator.visit(tree)

        # Guardamos el archivo Python generado
        with open(output_program_file, "w") as f:
            f.write(output_program)

        print("✔ CODEGEN OK")
        log.append("[CODEGEN] ✔ Python generado\n")

    except Exception as e:
        print("❌ Error en codegen:", e)
        log.append("[CODEGEN] Error: " + str(e))

        with open(output_text_file, "w") as f:
            f.write("\n".join(log))
        return

    # ======================================================
    # 7. EJECUCIÓN DEL PROGRAMA PYTHON GENERADO
    # ======================================================
    print(">>> EJECUTANDO PROGRAMA...")

    log.append("[PYTHON OUTPUT]\n")

    try:
        # Ejecutamos el archivo Python generado
        result = subprocess.run(
            ["python3", output_program_file],
            capture_output=True,
            text=True
        )
        print(result.stdout)        # Mostrar salida en consola
        log.append(result.stdout)   # Guardar salida en el log

    except Exception as e:
        print("❌ Error al ejecutar:", e)
        log.append("[RUNTIME] Error: " + str(e))

    # ======================================================
    # 8. GUARDAR LOG FINAL
    # ======================================================
    log.append("[FIN DEL PROCESO]\n")

    # Siempre guardamos el log al final de TODO
    with open(output_text_file, "w") as f:
        f.write("\n".join(log))

    print(f"✔ Proceso completado. Revisa {output_text_file} y {output_program_file}")


# ======================================================
# EJECUCIÓN DIRECTA DEL SCRIPT
# ======================================================
if __name__ == "__main__":
    main()
