grammar Expr;
prog: expr* EOF;
expr: create_stmt
| select_stmt
//| insert_stmt
;
create_stmt: 'CREATE' 'table' ID '(' column_list ')' ;
column_list: column_spec ( ',' column_spec )* ;
column_spec: ID ':' column_type;
column_type: 'string' | 'int';

IDS : ID ( ',' ID )* | '*';
ID : [a-zA-Z]+ ;

select_stmt: 'SELECT' IDS 'FROM' ID ('WHERE' CONDS)*;

CONDS: COND ('OR'| 'AND' COND)* ;
COND : ID '=' VAL ;
VAL : INT | STRING ;


//optr : [a-z];
NEWLINE : [\r\n]+ ;
INT : [0-9]+ ;
STRING: [a-z]+;
WS : [ \t\r\n] -> channel(HIDDEN);