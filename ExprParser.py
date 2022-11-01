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
        4,1,28,108,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,3,1,32,8,1,1,1,4,1,35,8,1,11,1,12,1,36,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,4,1,4,
        1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,67,8,6,10,6,12,6,
        70,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,79,8,7,10,7,12,7,82,9,7,5,
        7,84,8,7,10,7,12,7,87,9,7,1,8,1,8,1,8,1,8,5,8,93,8,8,10,8,12,8,96,
        9,8,1,8,3,8,99,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,0,0,10,0,2,4,
        6,8,10,12,14,16,18,0,3,1,0,8,9,1,0,13,14,1,0,19,24,107,0,23,1,0,
        0,0,2,31,1,0,0,0,4,38,1,0,0,0,6,45,1,0,0,0,8,53,1,0,0,0,10,57,1,
        0,0,0,12,59,1,0,0,0,14,73,1,0,0,0,16,88,1,0,0,0,18,103,1,0,0,0,20,
        22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,
        0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,32,3,
        4,2,0,29,32,3,12,6,0,30,32,3,14,7,0,31,28,1,0,0,0,31,29,1,0,0,0,
        31,30,1,0,0,0,32,34,1,0,0,0,33,35,5,1,0,0,34,33,1,0,0,0,35,36,1,
        0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,3,1,0,0,0,38,39,5,2,0,0,39,
        40,5,3,0,0,40,41,5,25,0,0,41,42,5,4,0,0,42,43,3,6,3,0,43,44,5,5,
        0,0,44,5,1,0,0,0,45,50,3,8,4,0,46,47,5,6,0,0,47,49,3,8,4,0,48,46,
        1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,7,1,0,0,0,52,
        50,1,0,0,0,53,54,5,25,0,0,54,55,5,7,0,0,55,56,3,10,5,0,56,9,1,0,
        0,0,57,58,7,0,0,0,58,11,1,0,0,0,59,60,5,10,0,0,60,61,5,11,0,0,61,
        62,5,25,0,0,62,63,5,4,0,0,63,68,5,18,0,0,64,65,5,6,0,0,65,67,5,18,
        0,0,66,64,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,71,
        1,0,0,0,70,68,1,0,0,0,71,72,5,5,0,0,72,13,1,0,0,0,73,85,3,16,8,0,
        74,75,5,12,0,0,75,80,3,18,9,0,76,77,7,1,0,0,77,79,3,18,9,0,78,76,
        1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,84,1,0,0,0,
        82,80,1,0,0,0,83,74,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,
        0,0,0,86,15,1,0,0,0,87,85,1,0,0,0,88,98,5,15,0,0,89,94,5,25,0,0,
        90,91,5,6,0,0,91,93,5,25,0,0,92,90,1,0,0,0,93,96,1,0,0,0,94,92,1,
        0,0,0,94,95,1,0,0,0,95,99,1,0,0,0,96,94,1,0,0,0,97,99,5,16,0,0,98,
        89,1,0,0,0,98,97,1,0,0,0,99,100,1,0,0,0,100,101,5,17,0,0,101,102,
        5,25,0,0,102,17,1,0,0,0,103,104,5,25,0,0,104,105,7,2,0,0,105,106,
        5,18,0,0,106,19,1,0,0,0,9,23,31,36,50,68,80,85,94,98
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'CREATE'", "'table'", "'('", "')'", 
                     "','", "':'", "'string'", "'int'", "'INSERT'", "'INTO'", 
                     "'WHERE'", "'OR'", "'AND'", "'SELECT'", "'*'", "'FROM'", 
                     "<INVALID>", "'='", "'>'", "'<'", "'>='", "'<='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "VAL", "EQ", "GR", "LS", 
                      "GEQ", "LEQ", "NEQ", "ID", "INT", "STRING", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_create_stmt = 2
    RULE_column_list = 3
    RULE_column_spec = 4
    RULE_column_type = 5
    RULE_insert_stmt = 6
    RULE_select_stmt = 7
    RULE_select = 8
    RULE_cond = 9

    ruleNames =  [ "prog", "expr", "create_stmt", "column_list", "column_spec", 
                   "column_type", "insert_stmt", "select_stmt", "select", 
                   "cond" ]

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
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    VAL=18
    EQ=19
    GR=20
    LS=21
    GEQ=22
    LEQ=23
    NEQ=24
    ID=25
    INT=26
    STRING=27
    WS=28

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
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 33796) != 0:
                self.state = 20
                self.expr()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
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


        def insert_stmt(self):
            return self.getTypedRuleContext(ExprParser.Insert_stmtContext,0)


        def select_stmt(self):
            return self.getTypedRuleContext(ExprParser.Select_stmtContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 28
                self.create_stmt()
                pass
            elif token in [10]:
                self.state = 29
                self.insert_stmt()
                pass
            elif token in [15]:
                self.state = 30
                self.select_stmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                self.match(ExprParser.T__0)
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

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
            self.state = 38
            self.match(ExprParser.T__1)
            self.state = 39
            self.match(ExprParser.T__2)
            self.state = 40
            self.match(ExprParser.ID)
            self.state = 41
            self.match(ExprParser.T__3)
            self.state = 42
            self.column_list()
            self.state = 43
            self.match(ExprParser.T__4)
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
            self.state = 45
            self.column_spec()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 46
                self.match(ExprParser.T__5)
                self.state = 47
                self.column_spec()
                self.state = 52
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
            self.state = 53
            self.match(ExprParser.ID)
            self.state = 54
            self.match(ExprParser.T__6)
            self.state = 55
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
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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


    class Insert_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def VAL(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.VAL)
            else:
                return self.getToken(ExprParser.VAL, i)

        def getRuleIndex(self):
            return ExprParser.RULE_insert_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert_stmt" ):
                listener.enterInsert_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert_stmt" ):
                listener.exitInsert_stmt(self)




    def insert_stmt(self):

        localctx = ExprParser.Insert_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_insert_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ExprParser.T__9)
            self.state = 60
            self.match(ExprParser.T__10)
            self.state = 61
            self.match(ExprParser.ID)
            self.state = 62
            self.match(ExprParser.T__3)
            self.state = 63
            self.match(ExprParser.VAL)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 64
                self.match(ExprParser.T__5)
                self.state = 65
                self.match(ExprParser.VAL)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select(self):
            return self.getTypedRuleContext(ExprParser.SelectContext,0)


        def cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.CondContext)
            else:
                return self.getTypedRuleContext(ExprParser.CondContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_select_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_stmt" ):
                listener.enterSelect_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_stmt" ):
                listener.exitSelect_stmt(self)




    def select_stmt(self):

        localctx = ExprParser.Select_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_select_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.select()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 74
                self.match(ExprParser.T__11)
                self.state = 75
                self.cond()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13 or _la==14:
                    self.state = 76
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 77
                    self.cond()
                    self.state = 82
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def getRuleIndex(self):
            return ExprParser.RULE_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect" ):
                listener.enterSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect" ):
                listener.exitSelect(self)




    def select(self):

        localctx = ExprParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_select)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ExprParser.T__14)
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 89
                self.match(ExprParser.ID)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 90
                    self.match(ExprParser.T__5)
                    self.state = 91
                    self.match(ExprParser.ID)
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [16]:
                self.state = 97
                self.match(ExprParser.T__15)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 100
            self.match(ExprParser.T__16)
            self.state = 101
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def VAL(self):
            return self.getToken(ExprParser.VAL, 0)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def GR(self):
            return self.getToken(ExprParser.GR, 0)

        def LS(self):
            return self.getToken(ExprParser.LS, 0)

        def GEQ(self):
            return self.getToken(ExprParser.GEQ, 0)

        def LEQ(self):
            return self.getToken(ExprParser.LEQ, 0)

        def NEQ(self):
            return self.getToken(ExprParser.NEQ, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = ExprParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ExprParser.ID)
            self.state = 104
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 105
            self.match(ExprParser.VAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





