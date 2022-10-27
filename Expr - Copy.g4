grammar Expr;
prog: expr* EOF;
expr: create_stmt
| select_stmt| insert_stmt
;
create_stmt: 'CREATE' 'table' ID '(' column_list ')' ;
column_list: column_spec ( ',' column_spec )* ;
column_spec: ID ':' column_type;
column_type: 'string' | 'int';

select_stmt: 'SELECT' IDS 'FROM' ID ('WHERE' COND);


COND : ID op VALUE;

IDS : ID ( ',' ID )* | '*';
ID : [a-z]+ ;
op : [+-*/];
NEWLINE : [\r\n]+ ;
INT : [0-9]+ ;
WS : [ \t\r\n] -> channel(HIDDEN);