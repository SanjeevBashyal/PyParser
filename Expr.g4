grammar Sql;
prog: expr* EOF;

expr: ((create_stmt | insert_stmt | select_stmt) ';'+)
;

create_stmt: 'CREATE' 'table' ID '(' column_list ')' ;
column_list: column_spec ( ',' column_spec )* ;
column_spec: ID ':' column_type;
column_type: 'string' | 'int';

insert_stmt: 'INSERT' 'INTO' ID '(' VAL ( ',' VAL )* ')' ;
VAL : INT | STRING ;

select_stmt: 'SELECT' ((ID (',' ID)*) | '*') 'FROM' ID ('WHERE' cond (('OR'| 'AND') cond)*)*;
cond : ID (EQ | GR | LS | GEQ | LEQ | NEQ) VAL ;

EQ: '=';
GR: '>';
LS: '<';
GEQ: '>=';
LEQ: '<=';
NEQ: '!=';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT : [0-9]+ ;
STRING: '"' (~('\n' | '"'))* '"';
COMMENT: '//' ~[\r\n]* -> skip;
WS : [ \t\r\n] -> channel(HIDDEN);