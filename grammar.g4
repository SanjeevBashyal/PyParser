grammar Expr;
prog: expr* EOF;
expr: create_stmt
| select_stmt| insert_stmt
;
create_stmt: 'CREATE' 'table' ID '(' column_list ')' ;
column_list: column_spec ( ',' column_spec )* ;
column_spec: ID ':' column_type;
Column_type: 'string' | 'int';
...
NEWLINE : [\r\n]+ ;
INT : [0-9]+ ;
WS : [ \t\r\n] -> channel(HIDDEN);