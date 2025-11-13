from generated.LogicaVisitor import LogicaVisitor  # Importa la clase base Visitor generada por ANTLR

# ===============================================================
# GENERADOR DE CÓDIGO PYTHON
# ===============================================================
class CodeGenerator(LogicaVisitor):
    """
    Visitor que recorre el AST y genera código Python equivalente
    al programa fuente en lenguaje lógico.
    """

    def __init__(self):
        self.lines = []            # Lista para almacenar líneas de código generadas
        self.indent = "    "       # Indentación estándar para bloques (4 espacios)

    # ============================================
    # PROGRAMA PRINCIPAL
    # ============================================
    def visitProgram(self, ctx):
        # Encabezado del código generado
        self.lines.append("# ============================================")
        self.lines.append("# Código generado automáticamente por MiniCompilador")
        self.lines.append("# NO MODIFICAR MANUALMENTE")
        self.lines.append("# ============================================")
        self.lines.append("")

        # Función auxiliar para convertir expresiones a booleano
        self.lines.append("def to_bool(value):")
        self.lines.append(self.indent + "\"\"\"Convierte expresiones a booleano explícito.\"\"\"")
        self.lines.append(self.indent + "return True if value is True else False")
        self.lines.append("")

        # Función principal del programa
        self.lines.append("def main():")
        self.lines.append(self.indent + "# --- Inicio del programa generado ---")

        # Recorrer y generar código de cada sentencia del programa
        for stmt in ctx.statement():
            code = self.visit(stmt)             # Genera código para la sentencia
            if code:
                for line in code.splitlines():  # Añade cada línea con la indentación correcta
                    self.lines.append(self.indent + line)

        self.lines.append(self.indent + "# --- Fin del programa generado ---")
        self.lines.append("")
        self.lines.append("if __name__ == '__main__':")
        self.lines.append(self.indent + "main()")   # Ejecuta la función principal

        return "\n".join(self.lines)  # Retorna todo el código generado como un string

    # ============================================
    # ASIGNACIÓN: ID = boolExpr;
    # ============================================
    def visitAssignment(self, ctx):
        var = ctx.ID().getText()          # Obtiene nombre de la variable
        expr = self.visit(ctx.boolExpr()) # Genera código para la expresión booleana
        return f"{var} = to_bool({expr})" # Asignación en Python con conversión explícita a bool

    # ============================================
    # PRINT: print(ID)
    # ============================================
    def visitPrintStmt(self, ctx):
        var = ctx.ID().getText()          # Obtiene la variable a imprimir
        return f"print(str({var}))  # print({var})"  # Genera print en Python con comentario

    # ============================================
    # IF / ELSE
    # ============================================
    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.boolExpr())      # Genera código de la condición
        then_block = self.visit(ctx.block(0))  # Genera código del bloque THEN

        code = [f"# --- IF ---", f"if {cond}:"] # Inicia la sentencia if
        for l in then_block.splitlines():      # Añade líneas del bloque THEN con indentación
            code.append(self.indent + l)

        if ctx.block(1):                        # Si existe bloque ELSE
            else_block = self.visit(ctx.block(1)) # Genera código del bloque ELSE
            code.append("else:")                 # Añade sentencia else
            for l in else_block.splitlines():    # Añade líneas del bloque ELSE con indentación
                code.append(self.indent + l)

        return "\n".join(code)                   # Retorna el código completo del if/else

    # ============================================
    # WHILE
    # ============================================
    def visitWhileStmt(self, ctx):
        cond = self.visit(ctx.boolExpr())       # Genera código de la condición
        body = self.visit(ctx.block())          # Genera código del cuerpo del while

        code = ["# --- WHILE ---", f"while {cond}:"]  # Inicia la sentencia while
        for l in body.splitlines():                   # Añade líneas del cuerpo con indentación
            code.append(self.indent + l)

        return "\n".join(code)                        # Retorna código completo del while

    # ============================================
    # BLOQUE { ... }
    # ============================================
    def visitBlock(self, ctx):
        output = []                          # Lista temporal para las líneas del bloque
        for stmt in ctx.statement():         # Recorre cada sentencia en el bloque
            s = self.visit(stmt)             # Genera código para la sentencia
            if s:
                output.extend(s.splitlines()) # Añade cada línea separada
        return "\n".join(output)             # Retorna código completo del bloque

    # ============================================
    # EXPRESIONES BOOLEANAS
    # ============================================
    def visitOrExpr(self, ctx):
        # Genera código para OR: (expr OR term)
        return f"({self.visit(ctx.boolExpr())} or {self.visit(ctx.boolTerm())})"

    def visitAndExpr(self, ctx):
        # Genera código para AND: (term AND factor)
        return f"({self.visit(ctx.boolTerm())} and {self.visit(ctx.boolFactor())})"

    def visitNotFactor(self, ctx):
        # Genera código para NOT factor
        return f"(not {self.visit(ctx.boolFactor())})"

    def visitParenExpr(self, ctx):
        # Genera código para expresión entre paréntesis
        return f"({self.visit(ctx.boolExpr())})"

    # ============================================
    # TERMINALES
    # ============================================
    def visitIdExpr(self, ctx):
        return ctx.ID().getText()  # Devuelve el nombre de la variable como cadena

    def visitTrueExpr(self, ctx):
        return "True"              # Devuelve True en Python

    def visitFalseExpr(self, ctx):
        return "False"             # Devuelve False en Python
