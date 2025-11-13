from generated.LogicaVisitor import LogicaVisitor
from generated.LogicaParser import LogicaParser
from .symbol_table import SymbolTable

class SemanticAnalyzer(LogicaVisitor):

    def __init__(self):
        self.symbols = SymbolTable()
        self.errors = []

    def visitProgram(self, ctx):
        ok = True
        for stmt in ctx.statement():
            if not self.visit(stmt):
                ok = False
        return ok

    def visitBlock(self, ctx):
        ok = True
        for stmt in ctx.statement():
            if not self.visit(stmt):
                ok = False
        return ok

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        expr_ok = self.visit(ctx.boolExpr())

        if not self.symbols.exists(var_name):
            self.symbols.declare(var_name)

        return expr_ok

    def visitPrintStmt(self, ctx):
        name = ctx.ID().getText()

        if not self.symbols.exists(name):
            self.errors.append(f"[Error] Variable '{name}' no declarada antes de print().")
            return False

        return True

    def visitIfStmt(self, ctx):
        cond_ok = self.visit(ctx.boolExpr())
        then_ok = self.visit(ctx.block(0))
        else_ok = True

        if ctx.block(1):
            else_ok = self.visit(ctx.block(1))

        return cond_ok and then_ok and else_ok

    def visitWhileStmt(self, ctx):
        cond_ok = self.visit(ctx.boolExpr())
        body_ok = self.visit(ctx.block())
        return cond_ok and body_ok

    def visitOrExpr(self, ctx):
        return self.visit(ctx.boolExpr()) and self.visit(ctx.boolTerm())

    def visitAndExpr(self, ctx):
        return self.visit(ctx.boolTerm()) and self.visit(ctx.boolFactor())

    def visitNotFactor(self, ctx):
        return self.visit(ctx.boolFactor())

    def visitParenExpr(self, ctx):
        return self.visit(ctx.boolExpr())

    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()

        if not self.symbols.exists(name):
            self.errors.append(f"[Error] Variable '{name}' usada sin declarar.")
            return False

        return True

    def visitTrueExpr(self, ctx):
        return True

    def visitFalseExpr(self, ctx):
        return True