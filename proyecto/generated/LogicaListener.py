# Generated from Logica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LogicaParser import LogicaParser
else:
    from LogicaParser import LogicaParser

# This class defines a complete listener for a parse tree produced by LogicaParser.
class LogicaListener(ParseTreeListener):

    # Enter a parse tree produced by LogicaParser#program.
    def enterProgram(self, ctx:LogicaParser.ProgramContext):
        pass

    # Exit a parse tree produced by LogicaParser#program.
    def exitProgram(self, ctx:LogicaParser.ProgramContext):
        pass


    # Enter a parse tree produced by LogicaParser#statement.
    def enterStatement(self, ctx:LogicaParser.StatementContext):
        pass

    # Exit a parse tree produced by LogicaParser#statement.
    def exitStatement(self, ctx:LogicaParser.StatementContext):
        pass


    # Enter a parse tree produced by LogicaParser#assignment.
    def enterAssignment(self, ctx:LogicaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LogicaParser#assignment.
    def exitAssignment(self, ctx:LogicaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LogicaParser#printStmt.
    def enterPrintStmt(self, ctx:LogicaParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by LogicaParser#printStmt.
    def exitPrintStmt(self, ctx:LogicaParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by LogicaParser#ifStmt.
    def enterIfStmt(self, ctx:LogicaParser.IfStmtContext):
        pass

    # Exit a parse tree produced by LogicaParser#ifStmt.
    def exitIfStmt(self, ctx:LogicaParser.IfStmtContext):
        pass


    # Enter a parse tree produced by LogicaParser#whileStmt.
    def enterWhileStmt(self, ctx:LogicaParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by LogicaParser#whileStmt.
    def exitWhileStmt(self, ctx:LogicaParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by LogicaParser#block.
    def enterBlock(self, ctx:LogicaParser.BlockContext):
        pass

    # Exit a parse tree produced by LogicaParser#block.
    def exitBlock(self, ctx:LogicaParser.BlockContext):
        pass


    # Enter a parse tree produced by LogicaParser#toTerm.
    def enterToTerm(self, ctx:LogicaParser.ToTermContext):
        pass

    # Exit a parse tree produced by LogicaParser#toTerm.
    def exitToTerm(self, ctx:LogicaParser.ToTermContext):
        pass


    # Enter a parse tree produced by LogicaParser#orExpr.
    def enterOrExpr(self, ctx:LogicaParser.OrExprContext):
        pass

    # Exit a parse tree produced by LogicaParser#orExpr.
    def exitOrExpr(self, ctx:LogicaParser.OrExprContext):
        pass


    # Enter a parse tree produced by LogicaParser#toFactor.
    def enterToFactor(self, ctx:LogicaParser.ToFactorContext):
        pass

    # Exit a parse tree produced by LogicaParser#toFactor.
    def exitToFactor(self, ctx:LogicaParser.ToFactorContext):
        pass


    # Enter a parse tree produced by LogicaParser#andExpr.
    def enterAndExpr(self, ctx:LogicaParser.AndExprContext):
        pass

    # Exit a parse tree produced by LogicaParser#andExpr.
    def exitAndExpr(self, ctx:LogicaParser.AndExprContext):
        pass


    # Enter a parse tree produced by LogicaParser#notFactor.
    def enterNotFactor(self, ctx:LogicaParser.NotFactorContext):
        pass

    # Exit a parse tree produced by LogicaParser#notFactor.
    def exitNotFactor(self, ctx:LogicaParser.NotFactorContext):
        pass


    # Enter a parse tree produced by LogicaParser#parenExpr.
    def enterParenExpr(self, ctx:LogicaParser.ParenExprContext):
        pass

    # Exit a parse tree produced by LogicaParser#parenExpr.
    def exitParenExpr(self, ctx:LogicaParser.ParenExprContext):
        pass


    # Enter a parse tree produced by LogicaParser#idExpr.
    def enterIdExpr(self, ctx:LogicaParser.IdExprContext):
        pass

    # Exit a parse tree produced by LogicaParser#idExpr.
    def exitIdExpr(self, ctx:LogicaParser.IdExprContext):
        pass


    # Enter a parse tree produced by LogicaParser#trueExpr.
    def enterTrueExpr(self, ctx:LogicaParser.TrueExprContext):
        pass

    # Exit a parse tree produced by LogicaParser#trueExpr.
    def exitTrueExpr(self, ctx:LogicaParser.TrueExprContext):
        pass


    # Enter a parse tree produced by LogicaParser#falseExpr.
    def enterFalseExpr(self, ctx:LogicaParser.FalseExprContext):
        pass

    # Exit a parse tree produced by LogicaParser#falseExpr.
    def exitFalseExpr(self, ctx:LogicaParser.FalseExprContext):
        pass



del LogicaParser