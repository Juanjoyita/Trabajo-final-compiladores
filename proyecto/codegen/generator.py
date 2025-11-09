from generated.LogicaVisitor import LogicaVisitor

class CodeGenerator(LogicaVisitor):

    def __init__(self):
        self.lines = []
        self.indent = "    "

    def visitProgram(self, ctx):
        self.lines.append("# Código generado por el MiniCompilador")
        self.lines.append("def main():")
        
        for stmt in ctx.statement():
            code = self.visit(stmt)
            if code:
                for line in code.splitlines():
                    self.lines.append(self.indent + line)

        self.lines.append("")
        self.lines.append("if __name__ == '__main__':")
        self.lines.append(self.indent + "main()")
        return "\n".join(self.lines)

    def visitAssignment(self, ctx):
        var = ctx.ID().getText()
        expr = self.visit(ctx.boolExpr())
        return f"{var} = {expr}"

    def visitPrintStmt(self, ctx):
        return f"print({ctx.ID().getText()})"

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.boolExpr())
        then_block = self.visit(ctx.block(0))

        code = [f"if {cond}:"]
        for l in then_block.splitlines():
            code.append(self.indent + l)

        if ctx.block(1):
            else_block = self.visit(ctx.block(1))
            code.append("else:")
            for l in else_block.splitlines():
                code.append(self.indent + l)

        return "\n".join(code)

    def visitWhileStmt(self, ctx):
        cond = self.visit(ctx.boolExpr())
        body = self.visit(ctx.block())

        code = [f"while {cond}:"]
        for l in body.splitlines():
            code.append(self.indent + l)

        return "\n".join(code)

    def visitBlock(self, ctx):
        output = []
        for stmt in ctx.statement():
            s = self.visit(stmt)
            if s:
                output.extend(s.splitlines())
        return "\n".join(output)

    def visitOrExpr(self, ctx):
        return f"({self.visit(ctx.boolExpr())} or {self.visit(ctx.boolTerm())})"

    def visitAndExpr(self, ctx):
        return f"({self.visit(ctx.boolTerm())} and {self.visit(ctx.boolFactor())})"

    def visitNotFactor(self, ctx):
        return f"(not {self.visit(ctx.boolFactor())})"

    def visitParenExpr(self, ctx):
        return f"({self.visit(ctx.boolExpr())})"

    def visitIdExpr(self, ctx):
        return ctx.ID().getText()

    def visitTrueExpr(self, ctx):
        return "True"

    def visitFalseExpr(self, ctx):
        return "False"
