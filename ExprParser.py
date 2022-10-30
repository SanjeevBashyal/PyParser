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
        4,1,29,85,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,5,1,31,8,1,10,1,12,1,34,9,1,3,1,36,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,5,3,48,8,3,10,3,12,3,51,9,3,1,4,1,4,1,4,
        1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,65,8,6,10,6,12,6,68,9,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,80,8,8,10,8,12,8,83,
        9,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,8,9,82,0,21,1,0,0,0,
        2,35,1,0,0,0,4,37,1,0,0,0,6,44,1,0,0,0,8,52,1,0,0,0,10,56,1,0,0,
        0,12,58,1,0,0,0,14,69,1,0,0,0,16,76,1,0,0,0,18,20,3,2,1,0,19,18,
        1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,
        23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,36,3,4,2,0,27,36,3,12,
        6,0,28,32,3,14,7,0,29,31,5,1,0,0,30,29,1,0,0,0,31,34,1,0,0,0,32,
        30,1,0,0,0,32,33,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,35,26,1,0,0,
        0,35,27,1,0,0,0,35,28,1,0,0,0,36,3,1,0,0,0,37,38,5,2,0,0,38,39,5,
        3,0,0,39,40,5,25,0,0,40,41,5,4,0,0,41,42,3,6,3,0,42,43,5,5,0,0,43,
        5,1,0,0,0,44,49,3,8,4,0,45,46,5,6,0,0,46,48,3,8,4,0,47,45,1,0,0,
        0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,7,1,0,0,0,51,49,1,
        0,0,0,52,53,5,25,0,0,53,54,5,7,0,0,54,55,3,10,5,0,55,9,1,0,0,0,56,
        57,7,0,0,0,57,11,1,0,0,0,58,59,5,10,0,0,59,60,5,15,0,0,60,61,5,11,
        0,0,61,66,5,25,0,0,62,63,5,12,0,0,63,65,5,16,0,0,64,62,1,0,0,0,65,
        68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,13,1,0,0,0,68,66,1,0,0,
        0,69,70,5,13,0,0,70,71,5,14,0,0,71,72,5,25,0,0,72,73,5,4,0,0,73,
        74,3,16,8,0,74,75,5,5,0,0,75,15,1,0,0,0,76,81,5,18,0,0,77,78,5,6,
        0,0,78,80,5,18,0,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,
        82,1,0,0,0,82,17,1,0,0,0,83,81,1,0,0,0,6,21,32,35,49,66,81
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'CREATE'", "'table'", "'('", "')'", 
                     "','", "':'", "'string'", "'int'", "'SELECT'", "'FROM'", 
                     "'WHERE'", "'INSERT'", "'INTO'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'='", "'>'", "'<'", "'>='", 
                     "'<='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDS", "CONDS", 
                      "COND", "VAL", "EQ", "GR", "LS", "GEQ", "LEQ", "NEQ", 
                      "ID", "NEWLINE", "INT", "STRING", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_create_stmt = 2
    RULE_column_list = 3
    RULE_column_spec = 4
    RULE_column_type = 5
    RULE_select_stmt = 6
    RULE_insert_stmt = 7
    RULE_data = 8

    ruleNames =  [ "prog", "expr", "create_stmt", "column_list", "column_spec", 
                   "column_type", "select_stmt", "insert_stmt", "data" ]

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
    IDS=15
    CONDS=16
    COND=17
    VAL=18
    EQ=19
    GR=20
    LS=21
    GEQ=22
    LEQ=23
    NEQ=24
    ID=25
    NEWLINE=26
    INT=27
    STRING=28
    WS=29

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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 9220) != 0:
                self.state = 18
                self.expr()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
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


        def select_stmt(self):
            return self.getTypedRuleContext(ExprParser.Select_stmtContext,0)


        def insert_stmt(self):
            return self.getTypedRuleContext(ExprParser.Insert_stmtContext,0)


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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.create_stmt()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.select_stmt()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.insert_stmt()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 29
                    self.match(ExprParser.T__0)
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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
            self.state = 37
            self.match(ExprParser.T__1)
            self.state = 38
            self.match(ExprParser.T__2)
            self.state = 39
            self.match(ExprParser.ID)
            self.state = 40
            self.match(ExprParser.T__3)
            self.state = 41
            self.column_list()
            self.state = 42
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
            self.state = 44
            self.column_spec()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 45
                self.match(ExprParser.T__5)
                self.state = 46
                self.column_spec()
                self.state = 51
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
            self.state = 52
            self.match(ExprParser.ID)
            self.state = 53
            self.match(ExprParser.T__6)
            self.state = 54
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
            self.state = 56
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


    class Select_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDS(self):
            return self.getToken(ExprParser.IDS, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def CONDS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.CONDS)
            else:
                return self.getToken(ExprParser.CONDS, i)

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
        self.enterRule(localctx, 12, self.RULE_select_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ExprParser.T__9)
            self.state = 59
            self.match(ExprParser.IDS)
            self.state = 60
            self.match(ExprParser.T__10)
            self.state = 61
            self.match(ExprParser.ID)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 62
                self.match(ExprParser.T__11)
                self.state = 63
                self.match(ExprParser.CONDS)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def data(self):
            return self.getTypedRuleContext(ExprParser.DataContext,0)


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
        self.enterRule(localctx, 14, self.RULE_insert_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(ExprParser.T__12)
            self.state = 70
            self.match(ExprParser.T__13)
            self.state = 71
            self.match(ExprParser.ID)
            self.state = 72
            self.match(ExprParser.T__3)
            self.state = 73
            self.data()
            self.state = 74
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.VAL)
            else:
                return self.getToken(ExprParser.VAL, i)

        def getRuleIndex(self):
            return ExprParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)




    def data(self):

        localctx = ExprParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(ExprParser.VAL)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 77
                self.match(ExprParser.T__5)
                self.state = 78
                self.match(ExprParser.VAL)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





