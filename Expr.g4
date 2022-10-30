grammar Expr;
prog: expr* EOF;
expr: create_stmt
| select_stmt
| insert_stmt ';'*
;
create_stmt: 'CREATE' 'table' ID '(' column_list ')' ;
column_list: column_spec ( ',' column_spec )* ;
column_spec: ID ':' column_type;
column_type: 'string' | 'int';

IDS : ID ( ',' ID )* | '*';


select_stmt: 'SELECT' IDS 'FROM' ID ('WHERE' CONDS)*;

CONDS: COND (('OR'| 'AND') COND)* ;
COND : ID ('=' | '>' | '<' | '>=' | '<=' | '!=') VAL ;
VAL : INT | '"' STRING '"' ;

insert_stmt: 'INSERT' 'INTO' ID '(' data ')' ;
data: VAL ( ',' VAL )* ;

EQ: '=';
GR: '>';
LS: '<';
GEQ: '>=';
LEQ: '<=';
NEQ: '!=';

ID: [a-zA-Z]+;
NEWLINE : [\r\n]+ ;
INT : [0-9]+ ;
STRING: '"' (~('\n' | '"'))* '"';
WS : [ \t\r\n] -> channel(HIDDEN);