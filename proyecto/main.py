import sys                   # Permite leer argumentos desde la terminal (input.txt)
import subprocess            # Se usa para ejecutar el código Python generado
from antlr4 import *         # Librerías base de ANTLR para lexer/parser
import os                    # Manejo de archivos y rutas del sistema

# Importación del Lexer y Parser generados por ANTLR
from generated.LogicaLexer import LogicaLexer
from generated.LogicaParser import LogicaParser

# Listeners personalizados para errores y el analizador semántico
from semantic_analyzer.semantic_visitor import SemanticAnalyzer
from semantic_analyzer.listener import LexerErrorListener, SyntaxErrorListener

# Generador de código Python final
from codegen.generator import CodeGenerator

# Generador de IR (intermediate representation / código de 3 direcciones)
from codegen.ir_generator import IRGenerator


# ======================================================
# FUNCIÓN PARA IMPRIMIR EL ÁRBOL SINTÁCTICO JERÁRQUICO
# ======================================================
def print_tree(node, rule_names, indent=""):
    """Imprime el árbol sintáctico con indentación."""
    if node.getChildCount() == 0:
        print(indent + f"- {node.getText()}")
        return

    rule_name = rule_names[node.getRuleIndex()]
    print(indent + f"[{rule_name}]")

    for i in range(node.getChildCount()):
        print_tree(node.getChild(i), rule_names, indent + "  ")


# ======================================================
# MAIN PRINCIPAL DEL COMPILADOR
# ======================================================
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

    # ======================================================
    # 1. LECTURA DEL ARCHIVO
    # ======================================================
    log.append("[INPUT]\n")
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            log.append(f.read() + "\n")
    except:
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

    lexer_errors = LexerErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_errors)

    tokens = CommonTokenStream(lexer)
    tokens.fill()

    if lexer_errors.errors:
        log.append("[LÉXICOS]\n")
        for e in lexer_errors.errors:
            log.append("  - " + e)
        print("❌ Error léxico.")
        return

    print("✔ Léxico OK")
    log.append("[LÉXICOS] ✔ Sin errores\n")

    # ======================================================
    # 3. FASE SINTÁCTICA
    # ======================================================
    print(">>> FASE SINTÁCTICA...")

    parser = LogicaParser(tokens)

    syntax_errors = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(syntax_errors)

    tree = parser.program()

    if syntax_errors.errors:
        log.append("[SINTÁCTICOS]\n")
        for e in syntax_errors.errors:
            log.append("  - " + e)
        print("❌ Error sintáctico.")
        return

    print("✔ Sintaxis OK")
    log.append("[SINTÁCTICOS] ✔ Sin errores\n")

    # ======================================================
    # 4. FASE SEMÁNTICA
    # ======================================================
    print(">>> FASE SEMÁNTICA...")

    analyzer = SemanticAnalyzer()
    analyzer.visit(tree)

    if analyzer.errors:
        log.append("[SEMÁNTICA]\n")
        for e in analyzer.errors:
            log.append("  - " + e)
        print("❌ Error semántico.")
        return

    print("✔ Semántica OK")
    log.append("[SEMÁNTICA] ✔ Sin errores\n")

    # ======================================================
    # 5. FASE IR (TAC / INTERMEDIATE REPRESENTATION)
    # ======================================================
    print(">>> GENERANDO IR (Intermediate Representation)...")

    ir_generator = IRGenerator()
    ir_code = ir_generator.visit(tree)

    print("✔ IR generado correctamente.\n")
    print("=== CÓDIGO IR ===")
    for instr in ir_code:
        print(instr)

    log.append("[IR] ✔ IR generado\n")
    for instr in ir_code:
        log.append("  " + instr)

    # ======================================================
    # 6. GENERACIÓN DE CÓDIGO PYTHON
    # ======================================================
    print(">>> GENERANDO CÓDIGO PYTHON...")

    generator = CodeGenerator()
    output_program = generator.visit(tree)

    with open(output_program_file, "w") as f:
        f.write(output_program)

    print("✔ CODEGEN OK")
    log.append("[CODEGEN] ✔ Python generado\n")

    # ======================================================
    # 7. EJECUCIÓN DEL CÓDIGO PYTHON
    # ======================================================
    print(">>> EJECUTANDO PROGRAMA...")

    log.append("[PYTHON OUTPUT]\n")

    try:
        result = subprocess.run(
            ["python3", output_program_file],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        log.append(result.stdout)
    except Exception as e:
        print("❌ Error al ejecutar:", e)
        log.append(str(e))

    # ======================================================
    # 8. GUARDAR LOG FINAL
    # ======================================================
    log.append("[FIN DEL PROCESO]\n")
    with open(output_text_file, "w") as f:
        f.write("\n".join(log))

    print(f"✔ Proceso completado. Revisa {output_text_file} y {output_program_file}")


if __name__ == "__main__":
    main()
