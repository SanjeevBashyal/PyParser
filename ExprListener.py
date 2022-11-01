# Generated from Expr.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#create_stmt.
    def enterCreate_stmt(self, ctx:ExprParser.Create_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#create_stmt.
    def exitCreate_stmt(self, ctx:ExprParser.Create_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#column_list.
    def enterColumn_list(self, ctx:ExprParser.Column_listContext):
        pass

    # Exit a parse tree produced by ExprParser#column_list.
    def exitColumn_list(self, ctx:ExprParser.Column_listContext):
        pass


    # Enter a parse tree produced by ExprParser#column_spec.
    def enterColumn_spec(self, ctx:ExprParser.Column_specContext):
        pass

    # Exit a parse tree produced by ExprParser#column_spec.
    def exitColumn_spec(self, ctx:ExprParser.Column_specContext):
        pass


    # Enter a parse tree produced by ExprParser#column_type.
    def enterColumn_type(self, ctx:ExprParser.Column_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#column_type.
    def exitColumn_type(self, ctx:ExprParser.Column_typeContext):
        pass


    # Enter a parse tree produced by ExprParser#insert_stmt.
    def enterInsert_stmt(self, ctx:ExprParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#insert_stmt.
    def exitInsert_stmt(self, ctx:ExprParser.Insert_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#select_stmt.
    def enterSelect_stmt(self, ctx:ExprParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#select_stmt.
    def exitSelect_stmt(self, ctx:ExprParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#select.
    def enterSelect(self, ctx:ExprParser.SelectContext):
        pass

    # Exit a parse tree produced by ExprParser#select.
    def exitSelect(self, ctx:ExprParser.SelectContext):
        pass


    # Enter a parse tree produced by ExprParser#cond.
    def enterCond(self, ctx:ExprParser.CondContext):
        pass

    # Exit a parse tree produced by ExprParser#cond.
    def exitCond(self, ctx:ExprParser.CondContext):
        pass



del ExprParser