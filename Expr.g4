grammar Expr;
prog: expr* EOF;

expr: ((create_stmt | insert_stmt | select_stmt) ';'+)
;

create_stmt: 'CREATE' 'table' ID '(' column_list ')' ;
column_list: column_spec ( ',' column_spec )* ;
column_spec: ID ':' column_type;
column_type: 'string' | 'int';

insert_stmt: 'INSERT' 'INTO' ID '(' VAL ( ',' VAL )* ')' ;
VAL : INT | STRING ;

select_stmt: select ('WHERE' cond (('OR'| 'AND') cond)*)*;
select: 'SELECT' ((ID (',' ID)*) | '*') 'FROM' ID ;
cond : ID (EQ | GR | LS | GEQ | LEQ | NEQ) VAL ;

EQ: '=';
GR: '>';
LS: '<';
GEQ: '>=';
LEQ: '<=';
NEQ: '!=';

ID: [a-zA-Z]+;
// NEWLINE : [\r\n]+ ;
INT : [0-9]+ ;
STRING: '"' (~('\n' | '"'))* '"';
WS : [ \t\r\n] -> channel(HIDDEN);