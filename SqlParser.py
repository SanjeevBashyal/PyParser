# Generated from Sql.g4 by ANTLR 4.11.1
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
        4,1,29,107,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,5,1,25,8,1,10,1,12,1,28,
        9,1,1,2,1,2,1,2,3,2,33,8,2,1,2,4,2,36,8,2,11,2,12,2,37,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,50,8,4,10,4,12,4,53,9,4,1,5,1,
        5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,68,8,7,10,7,12,
        7,71,9,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,79,8,8,10,8,12,8,82,9,8,1,8,
        3,8,85,8,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,93,8,8,10,8,12,8,96,9,8,5,
        8,98,8,8,10,8,12,8,101,9,8,1,9,1,9,1,9,1,9,1,9,0,0,10,0,2,4,6,8,
        10,12,14,16,18,0,3,1,0,8,9,1,0,16,17,1,0,19,24,106,0,20,1,0,0,0,
        2,26,1,0,0,0,4,32,1,0,0,0,6,39,1,0,0,0,8,46,1,0,0,0,10,54,1,0,0,
        0,12,58,1,0,0,0,14,60,1,0,0,0,16,74,1,0,0,0,18,102,1,0,0,0,20,21,
        3,2,1,0,21,22,5,0,0,1,22,1,1,0,0,0,23,25,3,4,2,0,24,23,1,0,0,0,25,
        28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,3,1,0,0,0,28,26,1,0,0,
        0,29,33,3,6,3,0,30,33,3,14,7,0,31,33,3,16,8,0,32,29,1,0,0,0,32,30,
        1,0,0,0,32,31,1,0,0,0,33,35,1,0,0,0,34,36,5,1,0,0,35,34,1,0,0,0,
        36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,5,1,0,0,0,39,40,5,2,
        0,0,40,41,5,3,0,0,41,42,5,25,0,0,42,43,5,4,0,0,43,44,3,8,4,0,44,
        45,5,5,0,0,45,7,1,0,0,0,46,51,3,10,5,0,47,48,5,6,0,0,48,50,3,10,
        5,0,49,47,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,9,
        1,0,0,0,53,51,1,0,0,0,54,55,5,25,0,0,55,56,5,7,0,0,56,57,3,12,6,
        0,57,11,1,0,0,0,58,59,7,0,0,0,59,13,1,0,0,0,60,61,5,10,0,0,61,62,
        5,11,0,0,62,63,5,25,0,0,63,64,5,4,0,0,64,69,5,18,0,0,65,66,5,6,0,
        0,66,68,5,18,0,0,67,65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,
        1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,5,5,0,0,73,15,1,0,0,0,
        74,84,5,12,0,0,75,80,5,25,0,0,76,77,5,6,0,0,77,79,5,25,0,0,78,76,
        1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,85,1,0,0,0,
        82,80,1,0,0,0,83,85,5,13,0,0,84,75,1,0,0,0,84,83,1,0,0,0,85,86,1,
        0,0,0,86,87,5,14,0,0,87,99,5,25,0,0,88,89,5,15,0,0,89,94,3,18,9,
        0,90,91,7,1,0,0,91,93,3,18,9,0,92,90,1,0,0,0,93,96,1,0,0,0,94,92,
        1,0,0,0,94,95,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,97,88,1,0,0,0,
        98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,17,1,0,0,0,101,99,
        1,0,0,0,102,103,5,25,0,0,103,104,7,2,0,0,104,105,5,18,0,0,105,19,
        1,0,0,0,9,26,32,37,51,69,80,84,94,99
    ]

class SqlParser ( Parser ):

    grammarFileName = "Sql.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'CREATE'", "'table'", "'('", "')'", 
                     "','", "':'", "'string'", "'int'", "'INSERT'", "'INTO'", 
                     "'SELECT'", "'*'", "'FROM'", "'WHERE'", "'OR'", "'AND'", 
                     "<INVALID>", "'='", "'>'", "'<'", "'>='", "'<='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "VAL", "EQ", "GR", "LS", 
                      "GEQ", "LEQ", "NEQ", "ID", "INT", "STRING", "COMMENT", 
                      "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_stmt = 2
    RULE_create_stmt = 3
    RULE_column_list = 4
    RULE_column_spec = 5
    RULE_column_type = 6
    RULE_insert_stmt = 7
    RULE_select_stmt = 8
    RULE_cond = 9

    ruleNames =  [ "prog", "expr", "stmt", "create_stmt", "column_list", 
                   "column_spec", "column_type", "insert_stmt", "select_stmt", 
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
    COMMENT=28
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

        def expr(self):
            return self.getTypedRuleContext(SqlParser.ExprContext,0)


        def EOF(self):
            return self.getToken(SqlParser.EOF, 0)

        def getRuleIndex(self):
            return SqlParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SqlParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.expr()
            self.state = 21
            self.match(SqlParser.EOF)
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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SqlParser.StmtContext)
            else:
                return self.getTypedRuleContext(SqlParser.StmtContext,i)


        def getRuleIndex(self):
            return SqlParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = SqlParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 5124) != 0:
                self.state = 23
                self.stmt()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_stmt(self):
            return self.getTypedRuleContext(SqlParser.Create_stmtContext,0)


        def insert_stmt(self):
            return self.getTypedRuleContext(SqlParser.Insert_stmtContext,0)


        def select_stmt(self):
            return self.getTypedRuleContext(SqlParser.Select_stmtContext,0)


        def getRuleIndex(self):
            return SqlParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = SqlParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 29
                self.create_stmt()
                pass
            elif token in [10]:
                self.state = 30
                self.insert_stmt()
                pass
            elif token in [12]:
                self.state = 31
                self.select_stmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.match(SqlParser.T__0)
                self.state = 37 
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
            return self.getToken(SqlParser.ID, 0)

        def column_list(self):
            return self.getTypedRuleContext(SqlParser.Column_listContext,0)


        def getRuleIndex(self):
            return SqlParser.RULE_create_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_stmt" ):
                listener.enterCreate_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_stmt" ):
                listener.exitCreate_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate_stmt" ):
                return visitor.visitCreate_stmt(self)
            else:
                return visitor.visitChildren(self)




    def create_stmt(self):

        localctx = SqlParser.Create_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_create_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(SqlParser.T__1)
            self.state = 40
            self.match(SqlParser.T__2)
            self.state = 41
            self.match(SqlParser.ID)
            self.state = 42
            self.match(SqlParser.T__3)
            self.state = 43
            self.column_list()
            self.state = 44
            self.match(SqlParser.T__4)
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
                return self.getTypedRuleContexts(SqlParser.Column_specContext)
            else:
                return self.getTypedRuleContext(SqlParser.Column_specContext,i)


        def getRuleIndex(self):
            return SqlParser.RULE_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list" ):
                listener.enterColumn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list" ):
                listener.exitColumn_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_list" ):
                return visitor.visitColumn_list(self)
            else:
                return visitor.visitChildren(self)




    def column_list(self):

        localctx = SqlParser.Column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.column_spec()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 47
                self.match(SqlParser.T__5)
                self.state = 48
                self.column_spec()
                self.state = 53
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
            return self.getToken(SqlParser.ID, 0)

        def column_type(self):
            return self.getTypedRuleContext(SqlParser.Column_typeContext,0)


        def getRuleIndex(self):
            return SqlParser.RULE_column_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_spec" ):
                listener.enterColumn_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_spec" ):
                listener.exitColumn_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_spec" ):
                return visitor.visitColumn_spec(self)
            else:
                return visitor.visitChildren(self)




    def column_spec(self):

        localctx = SqlParser.Column_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_column_spec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(SqlParser.ID)
            self.state = 55
            self.match(SqlParser.T__6)
            self.state = 56
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
            return SqlParser.RULE_column_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_type" ):
                listener.enterColumn_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_type" ):
                listener.exitColumn_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_type" ):
                return visitor.visitColumn_type(self)
            else:
                return visitor.visitChildren(self)




    def column_type(self):

        localctx = SqlParser.Column_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_column_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
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
            return self.getToken(SqlParser.ID, 0)

        def VAL(self, i:int=None):
            if i is None:
                return self.getTokens(SqlParser.VAL)
            else:
                return self.getToken(SqlParser.VAL, i)

        def getRuleIndex(self):
            return SqlParser.RULE_insert_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert_stmt" ):
                listener.enterInsert_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert_stmt" ):
                listener.exitInsert_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert_stmt" ):
                return visitor.visitInsert_stmt(self)
            else:
                return visitor.visitChildren(self)




    def insert_stmt(self):

        localctx = SqlParser.Insert_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_insert_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(SqlParser.T__9)
            self.state = 61
            self.match(SqlParser.T__10)
            self.state = 62
            self.match(SqlParser.ID)
            self.state = 63
            self.match(SqlParser.T__3)
            self.state = 64
            self.match(SqlParser.VAL)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 65
                self.match(SqlParser.T__5)
                self.state = 66
                self.match(SqlParser.VAL)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(SqlParser.T__4)
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SqlParser.ID)
            else:
                return self.getToken(SqlParser.ID, i)

        def cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SqlParser.CondContext)
            else:
                return self.getTypedRuleContext(SqlParser.CondContext,i)


        def getRuleIndex(self):
            return SqlParser.RULE_select_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_stmt" ):
                listener.enterSelect_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_stmt" ):
                listener.exitSelect_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_stmt" ):
                return visitor.visitSelect_stmt(self)
            else:
                return visitor.visitChildren(self)




    def select_stmt(self):

        localctx = SqlParser.Select_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_select_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(SqlParser.T__11)
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 75
                self.match(SqlParser.ID)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 76
                    self.match(SqlParser.T__5)
                    self.state = 77
                    self.match(SqlParser.ID)
                    self.state = 82
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [13]:
                self.state = 83
                self.match(SqlParser.T__12)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 86
            self.match(SqlParser.T__13)
            self.state = 87
            self.match(SqlParser.ID)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 88
                self.match(SqlParser.T__14)
                self.state = 89
                self.cond()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16 or _la==17:
                    self.state = 90
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==17):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 91
                    self.cond()
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getToken(SqlParser.ID, 0)

        def VAL(self):
            return self.getToken(SqlParser.VAL, 0)

        def EQ(self):
            return self.getToken(SqlParser.EQ, 0)

        def GR(self):
            return self.getToken(SqlParser.GR, 0)

        def LS(self):
            return self.getToken(SqlParser.LS, 0)

        def GEQ(self):
            return self.getToken(SqlParser.GEQ, 0)

        def LEQ(self):
            return self.getToken(SqlParser.LEQ, 0)

        def NEQ(self):
            return self.getToken(SqlParser.NEQ, 0)

        def getRuleIndex(self):
            return SqlParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = SqlParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(SqlParser.ID)
            self.state = 103
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 104
            self.match(SqlParser.VAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





