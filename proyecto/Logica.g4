grammar Logica;

program
    : statement+ EOF
    ;

// ----------------------
// SENTENCIAS
// ----------------------
statement
    : assignment
    | printStmt
    | ifStmt
    | whileStmt
    ;

assignment
    : ID '=' boolExpr ';'
    ;

printStmt
    : 'print' '(' ID ')' ';'
    ;

ifStmt
    : 'if' '(' boolExpr ')' block ('else' block)?
    ;

whileStmt
    : 'while' '(' boolExpr ')' block
    ;

block
    : '{' statement+ '}'
    ;

// ----------------------
// EXPRESSIONS (CON LABELS)
// ----------------------
boolExpr
    : boolExpr OR boolTerm        # orExpr
    | boolTerm                    # toTerm
    ;

boolTerm
    : boolTerm AND boolFactor     # andExpr
    | boolFactor                  # toFactor
    ;

boolFactor
    : NOT boolFactor              # notFactor
    | '(' boolExpr ')'            # parenExpr
    | ID                          # idExpr
    | TRUE                        # trueExpr
    | FALSE                       # falseExpr
    ;

// ----------------------
// TOKENS
// ----------------------
TRUE    : 'TRUE' ;
FALSE   : 'FALSE' ;
AND     : 'AND' ;
OR      : 'OR' ;
NOT     : 'NOT' ;

ID      : [a-zA-Z_] [a-zA-Z_0-9]* ;

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
