# Generated from Logica.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,101,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,52,8,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,6,1,6,4,6,62,8,6,11,6,12,6,63,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        7,5,7,74,8,7,10,7,12,7,77,9,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,85,8,8,
        10,8,12,8,88,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,99,8,9,
        1,9,0,2,14,16,10,0,2,4,6,8,10,12,14,16,18,0,0,102,0,21,1,0,0,0,2,
        31,1,0,0,0,4,33,1,0,0,0,6,38,1,0,0,0,8,44,1,0,0,0,10,53,1,0,0,0,
        12,59,1,0,0,0,14,67,1,0,0,0,16,78,1,0,0,0,18,98,1,0,0,0,20,22,3,
        2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,
        25,1,0,0,0,25,26,5,0,0,1,26,1,1,0,0,0,27,32,3,4,2,0,28,32,3,6,3,
        0,29,32,3,8,4,0,30,32,3,10,5,0,31,27,1,0,0,0,31,28,1,0,0,0,31,29,
        1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,34,5,16,0,0,34,35,5,1,0,0,
        35,36,3,14,7,0,36,37,5,2,0,0,37,5,1,0,0,0,38,39,5,3,0,0,39,40,5,
        4,0,0,40,41,5,16,0,0,41,42,5,5,0,0,42,43,5,2,0,0,43,7,1,0,0,0,44,
        45,5,6,0,0,45,46,5,4,0,0,46,47,3,14,7,0,47,48,5,5,0,0,48,51,3,12,
        6,0,49,50,5,7,0,0,50,52,3,12,6,0,51,49,1,0,0,0,51,52,1,0,0,0,52,
        9,1,0,0,0,53,54,5,8,0,0,54,55,5,4,0,0,55,56,3,14,7,0,56,57,5,5,0,
        0,57,58,3,12,6,0,58,11,1,0,0,0,59,61,5,9,0,0,60,62,3,2,1,0,61,60,
        1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,
        65,66,5,10,0,0,66,13,1,0,0,0,67,68,6,7,-1,0,68,69,3,16,8,0,69,75,
        1,0,0,0,70,71,10,2,0,0,71,72,5,14,0,0,72,74,3,16,8,0,73,70,1,0,0,
        0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,15,1,0,0,0,77,75,
        1,0,0,0,78,79,6,8,-1,0,79,80,3,18,9,0,80,86,1,0,0,0,81,82,10,2,0,
        0,82,83,5,13,0,0,83,85,3,18,9,0,84,81,1,0,0,0,85,88,1,0,0,0,86,84,
        1,0,0,0,86,87,1,0,0,0,87,17,1,0,0,0,88,86,1,0,0,0,89,90,5,15,0,0,
        90,99,3,18,9,0,91,92,5,4,0,0,92,93,3,14,7,0,93,94,5,5,0,0,94,99,
        1,0,0,0,95,99,5,16,0,0,96,99,5,11,0,0,97,99,5,12,0,0,98,89,1,0,0,
        0,98,91,1,0,0,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,19,
        1,0,0,0,7,23,31,51,63,75,86,98
    ]

class LogicaParser ( Parser ):

    grammarFileName = "Logica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'print'", "'('", "')'", 
                     "'if'", "'else'", "'while'", "'{'", "'}'", "'TRUE'", 
                     "'FALSE'", "'AND'", "'OR'", "'NOT'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TRUE", "FALSE", 
                      "AND", "OR", "NOT", "ID", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_printStmt = 3
    RULE_ifStmt = 4
    RULE_whileStmt = 5
    RULE_block = 6
    RULE_boolExpr = 7
    RULE_boolTerm = 8
    RULE_boolFactor = 9

    ruleNames =  [ "program", "statement", "assignment", "printStmt", "ifStmt", 
                   "whileStmt", "block", "boolExpr", "boolTerm", "boolFactor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    TRUE=11
    FALSE=12
    AND=13
    OR=14
    NOT=15
    ID=16
    WS=17
    COMMENT=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LogicaParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicaParser.StatementContext)
            else:
                return self.getTypedRuleContext(LogicaParser.StatementContext,i)


        def getRuleIndex(self):
            return LogicaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LogicaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 65864) != 0)):
                    break

            self.state = 25
            self.match(LogicaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(LogicaParser.AssignmentContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(LogicaParser.PrintStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(LogicaParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(LogicaParser.WhileStmtContext,0)


        def getRuleIndex(self):
            return LogicaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LogicaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.printStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.ifStmt()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.whileStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LogicaParser.ID, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(LogicaParser.BoolExprContext,0)


        def getRuleIndex(self):
            return LogicaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = LogicaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(LogicaParser.ID)
            self.state = 34
            self.match(LogicaParser.T__0)
            self.state = 35
            self.boolExpr(0)
            self.state = 36
            self.match(LogicaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LogicaParser.ID, 0)

        def getRuleIndex(self):
            return LogicaParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = LogicaParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(LogicaParser.T__2)
            self.state = 39
            self.match(LogicaParser.T__3)
            self.state = 40
            self.match(LogicaParser.ID)
            self.state = 41
            self.match(LogicaParser.T__4)
            self.state = 42
            self.match(LogicaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolExpr(self):
            return self.getTypedRuleContext(LogicaParser.BoolExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicaParser.BlockContext)
            else:
                return self.getTypedRuleContext(LogicaParser.BlockContext,i)


        def getRuleIndex(self):
            return LogicaParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = LogicaParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(LogicaParser.T__5)
            self.state = 45
            self.match(LogicaParser.T__3)
            self.state = 46
            self.boolExpr(0)
            self.state = 47
            self.match(LogicaParser.T__4)
            self.state = 48
            self.block()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 49
                self.match(LogicaParser.T__6)
                self.state = 50
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolExpr(self):
            return self.getTypedRuleContext(LogicaParser.BoolExprContext,0)


        def block(self):
            return self.getTypedRuleContext(LogicaParser.BlockContext,0)


        def getRuleIndex(self):
            return LogicaParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = LogicaParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(LogicaParser.T__7)
            self.state = 54
            self.match(LogicaParser.T__3)
            self.state = 55
            self.boolExpr(0)
            self.state = 56
            self.match(LogicaParser.T__4)
            self.state = 57
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicaParser.StatementContext)
            else:
                return self.getTypedRuleContext(LogicaParser.StatementContext,i)


        def getRuleIndex(self):
            return LogicaParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = LogicaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(LogicaParser.T__8)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.statement()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 65864) != 0)):
                    break

            self.state = 65
            self.match(LogicaParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogicaParser.RULE_boolExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ToTermContext(BoolExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.BoolExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolTerm(self):
            return self.getTypedRuleContext(LogicaParser.BoolTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToTerm" ):
                listener.enterToTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToTerm" ):
                listener.exitToTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToTerm" ):
                return visitor.visitToTerm(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(BoolExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.BoolExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolExpr(self):
            return self.getTypedRuleContext(LogicaParser.BoolExprContext,0)

        def OR(self):
            return self.getToken(LogicaParser.OR, 0)
        def boolTerm(self):
            return self.getTypedRuleContext(LogicaParser.BoolTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def boolExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LogicaParser.BoolExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_boolExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = LogicaParser.ToTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 68
            self.boolTerm(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LogicaParser.OrExprContext(self, LogicaParser.BoolExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                    self.state = 70
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 71
                    self.match(LogicaParser.OR)
                    self.state = 72
                    self.boolTerm(0) 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BoolTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogicaParser.RULE_boolTerm

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ToFactorContext(BoolTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.BoolTermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolFactor(self):
            return self.getTypedRuleContext(LogicaParser.BoolFactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToFactor" ):
                listener.enterToFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToFactor" ):
                listener.exitToFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToFactor" ):
                return visitor.visitToFactor(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(BoolTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.BoolTermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolTerm(self):
            return self.getTypedRuleContext(LogicaParser.BoolTermContext,0)

        def AND(self):
            return self.getToken(LogicaParser.AND, 0)
        def boolFactor(self):
            return self.getTypedRuleContext(LogicaParser.BoolFactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def boolTerm(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LogicaParser.BoolTermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_boolTerm, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = LogicaParser.ToFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 79
            self.boolFactor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LogicaParser.AndExprContext(self, LogicaParser.BoolTermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolTerm)
                    self.state = 81
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 82
                    self.match(LogicaParser.AND)
                    self.state = 83
                    self.boolFactor() 
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BoolFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogicaParser.RULE_boolFactor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TrueExprContext(BoolFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.BoolFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(LogicaParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueExpr" ):
                listener.enterTrueExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueExpr" ):
                listener.exitTrueExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueExpr" ):
                return visitor.visitTrueExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotFactorContext(BoolFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.BoolFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(LogicaParser.NOT, 0)
        def boolFactor(self):
            return self.getTypedRuleContext(LogicaParser.BoolFactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotFactor" ):
                listener.enterNotFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotFactor" ):
                listener.exitNotFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotFactor" ):
                return visitor.visitNotFactor(self)
            else:
                return visitor.visitChildren(self)


    class FalseExprContext(BoolFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.BoolFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(LogicaParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseExpr" ):
                listener.enterFalseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseExpr" ):
                listener.exitFalseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseExpr" ):
                return visitor.visitFalseExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(BoolFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.BoolFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolExpr(self):
            return self.getTypedRuleContext(LogicaParser.BoolExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(BoolFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogicaParser.BoolFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogicaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def boolFactor(self):

        localctx = LogicaParser.BoolFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_boolFactor)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = LogicaParser.NotFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(LogicaParser.NOT)
                self.state = 90
                self.boolFactor()
                pass
            elif token in [4]:
                localctx = LogicaParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(LogicaParser.T__3)
                self.state = 92
                self.boolExpr(0)
                self.state = 93
                self.match(LogicaParser.T__4)
                pass
            elif token in [16]:
                localctx = LogicaParser.IdExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.match(LogicaParser.ID)
                pass
            elif token in [11]:
                localctx = LogicaParser.TrueExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.match(LogicaParser.TRUE)
                pass
            elif token in [12]:
                localctx = LogicaParser.FalseExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 97
                self.match(LogicaParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.boolExpr_sempred
        self._predicates[8] = self.boolTerm_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def boolExpr_sempred(self, localctx:BoolExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def boolTerm_sempred(self, localctx:BoolTermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




