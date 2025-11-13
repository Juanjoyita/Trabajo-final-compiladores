grammar Logica;

// Programa raíz: uno o más statements hasta EOF
program
    : statement+ EOF
    ;

// Sentencias permitidas: asignación, print, if, while
statement
    : assignment
    | printStmt
    | ifStmt
    | whileStmt
    ;

// Asignación: ID = expresión booleana;
assignment
    : ID '=' boolExpr ';'
    ;

// Print: imprimir valor de una variable
printStmt
    : 'print' '(' ID ')' ';'
    ;

// If: condición booleana y bloque, opcional else
ifStmt
    : 'if' '(' boolExpr ')' block ('else' block)?
    ;

// While: condición booleana y bloque de repetición
whileStmt
    : 'while' '(' boolExpr ')' block
    ;

// Bloque de una o más sentencias
block
    : '{' statement+ '}'
    ;

// Expresiones booleanas: OR recursivo
boolExpr
    : boolExpr OR boolTerm        # orExpr
    | boolTerm                    # toTerm
    ;

// Expresiones booleanas: AND recursivo
boolTerm
    : boolTerm AND boolFactor     # andExpr
    | boolFactor                  # toFactor
    ;

// Factor booleano: NOT, paréntesis, ID o constantes
boolFactor
    : NOT boolFactor              # notFactor
    | '(' boolExpr ')'            # parenExpr
    | ID                          # idExpr
    | TRUE                        # trueExpr
    | FALSE                       # falseExpr
    ;

// Tokens reservados
TRUE    : 'TRUE' ;
FALSE   : 'FALSE' ;
AND     : 'AND' ;
OR      : 'OR' ;
NOT     : 'NOT' ;

// Identificador: letras o _ inicial, luego letras, números o _
ID      : [a-zA-Z_] [a-zA-Z_0-9]* ;

// Ignorar espacios y comentarios
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;

// Manejo de errores léxicos
INVALID_NUMBER : [0-9]+ ; // números no permitidos
ERROR_CHAR : . ;           // cualquier otro carácter inválido
