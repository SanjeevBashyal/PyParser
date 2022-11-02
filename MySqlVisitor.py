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
        if not table_name in self.columns:
            raise ValueError(f"Table {table_name} is not found")
        val=ctx.VAL()
        count=len(val)
        if count != len(self.columns[table_name]):
            raise ValueError(f"Column count and data count mismatch in table {table_name}")
        else:
            ls=[]
            for i in range(count):
                data_element=val[i].getText()
                data_seg=self.check_data_type(table_name,i,data_element)
                ls.append(data_seg)
                        
        self.data[table_name].append(ls)
        return self.visitChildren(ctx)    
    
    def visitSelect_stmt(self, ctx:SqlParser.Select_stmtContext):
        ids=ctx.ID()
        table_name=ids[-1].getText()
        total_number_of_columns=len(self.columns[table_name])
        all_columns=list(range(total_number_of_columns))
        columns_required=[]
        rows_required=list(range(len(self.data[table_name])))
        if ctx.getChild(1).getText()=='*':
            columns_required=all_columns
        else:
            check_list_of_columns=all_columns
            for i in range(len(ids)-1):
                column_name=ids[i].getText()
                for j in check_list_of_columns:
                    if column_name==self.columns[table_name][j][0]:
                        columns_required.append(j)
                        check_list_of_columns.remove(j)

        if len(ctx.cond())>0:
            rows_required=self.visitConditions(ctx.cond(), table_name, rows_required)

        data=self.fetch(table_name, columns_required, rows_required)
        self.show(data)

        return self.visitChildren(ctx)

    def visitConditions(self, condContextList, table_name, rows_required):
        for ctx in condContextList:
            column_name=ctx.ID().getText()
            operator=ctx.OP().getText()
            value=ctx.VAL().getText()
            column_index=self.check_column_index(table_name,column_name)
            value=self.check_data_type(table_name,column_index,value)
            selected_rows=[]
            for i in rows_required:
                to_check=self.data[table_name][i][column_index]
                flag=self.check_operator(operator,to_check,value)
                if flag:
                    selected_rows.append(i)
            rows_required=selected_rows
        return rows_required

    def visitCond(self, ctx:SqlParser.CondContext):
        return self.visitChildren(ctx)

    def fetch(self, table_name, columns_required, rows_required):
        column_names=[self.columns[table_name][j][0] for j in columns_required]
        data=[[self.data[table_name][i][j] for j in columns_required] for i in rows_required]
        data.insert(0,column_names)
        return data

    def show(self, data):
        print()
        for data_row in data:
            for data_element in data_row:
                print(data_element,'\t\t', end="", flush=True)               
            print()
        print()

    def check_column_index(self,table_name,column_name):
        for i,column_data in enumerate(self.columns[table_name]):
            if column_data[0]==column_name:
                return i

    def check_data_type(self,table_name,column_index,data):
        if self.columns[table_name][column_index][1]=='string':
            if data[0]!='"':
                raise ValueError(f"Column {self.columns[table_name][column_index][1]} of Table {table_name} requires string data type")
            else:
                return data[1:-1]
        else:
            if data[0]=='"':
                raise ValueError(f"Column {self.columns[table_name][column_index][1]} of Table {table_name} requires string int type")
            else:
                return int(data)

    def check_operator(self,operator,to_check,check_with):
        if operator=='=':
            if to_check == check_with:
                return True
            else:
                return False
        elif operator=='>':
            if to_check > check_with:
                return True
            else:
                return False
        elif operator=='<':
            if to_check < check_with:
                return True
            else:
                return False
        elif operator=='>=':
            if to_check >= check_with:
                return True
            else:
                return False
        elif operator=='<=':
            if to_check <= check_with:
                return True
            else:
                return False
        elif operator=='!=':
            if to_check != check_with:
                return True
            else:
                return False
