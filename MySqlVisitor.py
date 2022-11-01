from antlr4 import *
from SqlVisitor import SqlVisitor
from SqlParser import SqlParser

class MySqlVisitor(SqlVisitor):
    def __init__(self):
        self.stack = []
        self.tables = {}
        self.columns = {}
        self.data = {}
        
    def visitProg(self, ctx:SqlParser.ProgContext):
        return self.visit(ctx.expr()) # Just visit the self expression

    def visitCreate_stmt(self, ctx:SqlParser.Create_stmtContext):
        table_name=str(ctx.ID())
        if ctx.ID() in self.tables:
            raise ValueError(f"table {ctx.ID()} already exists")
        else:
            self.tables[ctx.ID()]=table_name
            self.columns[table_name]=[]
            self.data[table_name]=[]
        return self.visitChildren(ctx)

    def visitColumn_spec(self, ctx:SqlParser.Column_specContext):
        table_name=str(ctx.parentCtx.parentCtx.ID())
        column_name=str(ctx.ID())
        column_data=[column_name,ctx.column_type().getText()]
        self.columns[table_name].append(column_data)
        return self.visitChildren(ctx)

    def visitInsert_stmt(self, ctx:SqlParser.Insert_stmtContext):
        table_name=str(ctx.ID())
        val=ctx.VAL()
        count=len(val)
        if count != len(self.columns[table_name]):
            raise ValueError(f"Column count and data count mismatch in table {table_name}")
        else:
            ls=[]
            for i in range(count):
                data_element=val[i].getText()
                if self.columns[table_name][i][1]=='string':
                    if data_element[0]!='"':
                        raise ValueError(f"Column {self.columns[table_name][i][1]} of Table {table_name} requires string data type")
                    else:
                        ls.append(data_element[1:-1])
                else:
                    if data_element[0]=='"':
                        raise ValueError(f"Column {self.columns[table_name][i][1]} of Table {table_name} requires string int type")
                    else:
                        ls.append(data_element)
        self.data[table_name].append(ls)
        return self.visitChildren(ctx)    