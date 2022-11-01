# Generated from Sql.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete listener for a parse tree produced by SqlParser.
class SqlListener(ParseTreeListener):

    # Enter a parse tree produced by SqlParser#prog.
    def enterProg(self, ctx:SqlParser.ProgContext):
        pass

    # Exit a parse tree produced by SqlParser#prog.
    def exitProg(self, ctx:SqlParser.ProgContext):
        pass


    # Enter a parse tree produced by SqlParser#expr.
    def enterExpr(self, ctx:SqlParser.ExprContext):
        pass

    # Exit a parse tree produced by SqlParser#expr.
    def exitExpr(self, ctx:SqlParser.ExprContext):
        pass


    # Enter a parse tree produced by SqlParser#stmt.
    def enterStmt(self, ctx:SqlParser.StmtContext):
        pass

    # Exit a parse tree produced by SqlParser#stmt.
    def exitStmt(self, ctx:SqlParser.StmtContext):
        pass


    # Enter a parse tree produced by SqlParser#create_stmt.
    def enterCreate_stmt(self, ctx:SqlParser.Create_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#create_stmt.
    def exitCreate_stmt(self, ctx:SqlParser.Create_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#column_list.
    def enterColumn_list(self, ctx:SqlParser.Column_listContext):
        pass

    # Exit a parse tree produced by SqlParser#column_list.
    def exitColumn_list(self, ctx:SqlParser.Column_listContext):
        pass


    # Enter a parse tree produced by SqlParser#column_spec.
    def enterColumn_spec(self, ctx:SqlParser.Column_specContext):
        pass

    # Exit a parse tree produced by SqlParser#column_spec.
    def exitColumn_spec(self, ctx:SqlParser.Column_specContext):
        pass


    # Enter a parse tree produced by SqlParser#column_type.
    def enterColumn_type(self, ctx:SqlParser.Column_typeContext):
        pass

    # Exit a parse tree produced by SqlParser#column_type.
    def exitColumn_type(self, ctx:SqlParser.Column_typeContext):
        pass


    # Enter a parse tree produced by SqlParser#insert_stmt.
    def enterInsert_stmt(self, ctx:SqlParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#insert_stmt.
    def exitInsert_stmt(self, ctx:SqlParser.Insert_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#select_stmt.
    def enterSelect_stmt(self, ctx:SqlParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#select_stmt.
    def exitSelect_stmt(self, ctx:SqlParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#cond.
    def enterCond(self, ctx:SqlParser.CondContext):
        pass

    # Exit a parse tree produced by SqlParser#cond.
    def exitCond(self, ctx:SqlParser.CondContext):
        pass



del SqlParser