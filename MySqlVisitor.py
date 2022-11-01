import imp
from antlr4 import *
from SqlVisitor import SqlVisitor
from SqlParser import SqlParser

class MySqlVisitor(SqlVisitor):
    def __init__(self):
        self.stack = []
        self.tables = {}
    def visitProg(self, ctx:SqlParser.ProgContext):
        return self.visit(ctx.expr()) # Just visit the self expression
    def visitCreate_stmt(self, ctx:SqlParser.Create_stmtContext):
        print(ctx.getText())
        print(ctx.ID())
        if ctx.ID() in self.tables:
            raise ValueError(f"table {ctx.ID()} already exists")
        else:
            self.tables.update(ctx.ID():str(ctx.ID()))
        # Save the table definition in the dictionary