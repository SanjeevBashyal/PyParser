# Generated from Expr.g4 by ANTLR 4.11.1
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
        4,1,12,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,5,3,34,8,3,10,3,12,3,37,9,3,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,7,8,40,0,15,1,0,0,0,2,20,
        1,0,0,0,4,22,1,0,0,0,6,30,1,0,0,0,8,38,1,0,0,0,10,42,1,0,0,0,12,
        14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,
        0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,21,3,
        4,2,0,21,3,1,0,0,0,22,23,5,1,0,0,23,24,5,2,0,0,24,25,5,12,0,0,25,
        26,5,3,0,0,26,27,3,6,3,0,27,28,5,4,0,0,28,29,5,9,0,0,29,5,1,0,0,
        0,30,35,3,8,4,0,31,32,5,5,0,0,32,34,3,8,4,0,33,31,1,0,0,0,34,37,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,7,1,0,0,0,37,35,1,0,0,0,38,
        39,5,12,0,0,39,40,5,6,0,0,40,41,3,10,5,0,41,9,1,0,0,0,42,43,7,0,
        0,0,43,11,1,0,0,0,2,15,35
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'table'", "'('", "')'", "','", 
                     "':'", "'string'", "'int'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NEWLINE", "INT", "WS", "ID" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_create_stmt = 2
    RULE_column_list = 3
    RULE_column_spec = 4
    RULE_column_type = 5

    ruleNames =  [ "prog", "expr", "create_stmt", "column_list", "column_spec", 
                   "column_type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NEWLINE=9
    INT=10
    WS=11
    ID=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 12
                self.expr()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_stmt(self):
            return self.getTypedRuleContext(ExprParser.Create_stmtContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.create_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Create_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def column_list(self):
            return self.getTypedRuleContext(ExprParser.Column_listContext,0)


        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_create_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_stmt" ):
                listener.enterCreate_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_stmt" ):
                listener.exitCreate_stmt(self)




    def create_stmt(self):

        localctx = ExprParser.Create_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_create_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(ExprParser.T__0)
            self.state = 23
            self.match(ExprParser.T__1)
            self.state = 24
            self.match(ExprParser.ID)
            self.state = 25
            self.match(ExprParser.T__2)
            self.state = 26
            self.column_list()
            self.state = 27
            self.match(ExprParser.T__3)
            self.state = 28
            self.match(ExprParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Column_specContext)
            else:
                return self.getTypedRuleContext(ExprParser.Column_specContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list" ):
                listener.enterColumn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list" ):
                listener.exitColumn_list(self)




    def column_list(self):

        localctx = ExprParser.Column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.column_spec()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 31
                self.match(ExprParser.T__4)
                self.state = 32
                self.column_spec()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def column_type(self):
            return self.getTypedRuleContext(ExprParser.Column_typeContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_column_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_spec" ):
                listener.enterColumn_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_spec" ):
                listener.exitColumn_spec(self)




    def column_spec(self):

        localctx = ExprParser.Column_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_column_spec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ExprParser.ID)
            self.state = 39
            self.match(ExprParser.T__5)
            self.state = 40
            self.column_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_column_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_type" ):
                listener.enterColumn_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_type" ):
                listener.exitColumn_type(self)




    def column_type(self):

        localctx = ExprParser.Column_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_column_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





