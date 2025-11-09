# Generated from Logica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LogicaParser import LogicaParser
else:
    from LogicaParser import LogicaParser

# This class defines a complete generic visitor for a parse tree produced by LogicaParser.

class LogicaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LogicaParser#program.
    def visitProgram(self, ctx:LogicaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#statement.
    def visitStatement(self, ctx:LogicaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#assignment.
    def visitAssignment(self, ctx:LogicaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#printStmt.
    def visitPrintStmt(self, ctx:LogicaParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#ifStmt.
    def visitIfStmt(self, ctx:LogicaParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#whileStmt.
    def visitWhileStmt(self, ctx:LogicaParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#block.
    def visitBlock(self, ctx:LogicaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#toTerm.
    def visitToTerm(self, ctx:LogicaParser.ToTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#orExpr.
    def visitOrExpr(self, ctx:LogicaParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#toFactor.
    def visitToFactor(self, ctx:LogicaParser.ToFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#andExpr.
    def visitAndExpr(self, ctx:LogicaParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#notFactor.
    def visitNotFactor(self, ctx:LogicaParser.NotFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#parenExpr.
    def visitParenExpr(self, ctx:LogicaParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#idExpr.
    def visitIdExpr(self, ctx:LogicaParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#trueExpr.
    def visitTrueExpr(self, ctx:LogicaParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogicaParser#falseExpr.
    def visitFalseExpr(self, ctx:LogicaParser.FalseExprContext):
        return self.visitChildren(ctx)



del LogicaParser