from generated.LogicaVisitor import LogicaVisitor

class CodeGenerator(LogicaVisitor):

    def __init__(self):
        self.lines = []
        self.indent = "    "

    # ============================================
    #   PROGRAMA PRINCIPAL
    # ============================================
    def visitProgram(self, ctx):
        self.lines.append("# ============================================")
        self.lines.append("# Código generado automáticamente por MiniCompilador")
        self.lines.append("# NO MODIFICAR MANUALMENTE")
        self.lines.append("# ============================================")
        self.lines.append("")
        self.lines.append("def to_bool(value):")
        self.lines.append(self.indent + "\"\"\"Convierte expresiones a booleano explícito.\"\"\"")
        self.lines.append(self.indent + "return True if value is True else False")
        self.lines.append("")
        self.lines.append("def main():")
        self.lines.append(self.indent + "# --- Inicio del programa generado ---")

        # Sentencias principales
        for stmt in ctx.statement():
            code = self.visit(stmt)
            if code:
                for line in code.splitlines():
                    self.lines.append(self.indent + line)

        self.lines.append(self.indent + "# --- Fin del programa generado ---")
        self.lines.append("")
        self.lines.append("if __name__ == '__main__':")
        self.lines.append(self.indent + "main()")

        return "\n".join(self.lines)

    # ============================================
    #   ASIGNACIÓN
    # ============================================
    def visitAssignment(self, ctx):
        var = ctx.ID().getText()
        expr = self.visit(ctx.boolExpr())
        return f"{var} = to_bool({expr})"

    # ============================================
    #   PRINT
    # ============================================
    def visitPrintStmt(self, ctx):
        var = ctx.ID().getText()
        return f"print(str({var}))  # print({var})"

    # ============================================
    #   IF / ELSE
    # ============================================
    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.boolExpr())
        then_block = self.visit(ctx.block(0))

        code = [f"# --- IF ---", f"if {cond}:"]
        for l in then_block.splitlines():
            code.append(self.indent + l)

        if ctx.block(1):
            else_block = self.visit(ctx.block(1))
            code.append("else:")
            for l in else_block.splitlines():
                code.append(self.indent + l)

        return "\n".join(code)

    # ============================================
    #   WHILE
    # ============================================
    def visitWhileStmt(self, ctx):
        cond = self.visit(ctx.boolExpr())
        body = self.visit(ctx.block())

        code = ["# --- WHILE ---", f"while {cond}:"]
        for l in body.splitlines():
            code.append(self.indent + l)

        return "\n".join(code)

    # ============================================
    #   BLOQUE { ... }
    # ============================================
    def visitBlock(self, ctx):
        output = []
        for stmt in ctx.statement():
            s = self.visit(stmt)
            if s:
                output.extend(s.splitlines())
        return "\n".join(output)

    # ============================================
    #   EXPRESIONES BOOLEANAS
    # ============================================
    def visitOrExpr(self, ctx):
        return f"({self.visit(ctx.boolExpr())} or {self.visit(ctx.boolTerm())})"

    def visitAndExpr(self, ctx):
        return f"({self.visit(ctx.boolTerm())} and {self.visit(ctx.boolFactor())})"

    def visitNotFactor(self, ctx):
        return f"(not {self.visit(ctx.boolFactor())})"

    def visitParenExpr(self, ctx):
        return f"({self.visit(ctx.boolExpr())})"

    # ============================================
    #   TERMINALES
    # ============================================
    def visitIdExpr(self, ctx):
        return ctx.ID().getText()

    def visitTrueExpr(self, ctx):
        return "True"

    def visitFalseExpr(self, ctx):
        return "False"
