# Generated from Sql.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete generic visitor for a parse tree produced by SqlParser.

class SqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SqlParser#prog.
    def visitProg(self, ctx:SqlParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#expr.
    def visitExpr(self, ctx:SqlParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#stmt.
    def visitStmt(self, ctx:SqlParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#create_stmt.
    def visitCreate_stmt(self, ctx:SqlParser.Create_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#column_list.
    def visitColumn_list(self, ctx:SqlParser.Column_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#column_spec.
    def visitColumn_spec(self, ctx:SqlParser.Column_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#column_type.
    def visitColumn_type(self, ctx:SqlParser.Column_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#insert_stmt.
    def visitInsert_stmt(self, ctx:SqlParser.Insert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#select_stmt.
    def visitSelect_stmt(self, ctx:SqlParser.Select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#cond.
    def visitCond(self, ctx:SqlParser.CondContext):
        return self.visitChildren(ctx)



del SqlParser