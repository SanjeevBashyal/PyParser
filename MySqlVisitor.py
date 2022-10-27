
class MySqlVisitor(ExprVisitor):
    def __init__(self):
        self.stack = []
        self.tables = {}
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visit(ctx.expr()) # Just visit the self expression
    def visitCreateExpr(self, ctx:ExprParser.CreateExprContext):
        if ctx.ID() in self.tables:
            raise ValueError(f"table {ctx.ID()} already exists")
        # Save the table definition in the dictionary