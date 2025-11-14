grammar Logica;

// Regla principal valido cuando tenga una o mas sentencias y debe terminar en fin del archivo 
program
    : statement+ EOF
    ;

// Sentencias permitidas: asignación, print, if, while base del lenguaje 
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

// Print: imprimir valor de una variable y no imprime expresiones
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

// Expresiones booleanas: OR recursivo el cual tiene menor prioridad que AND 
boolExpr
    : boolExpr OR boolTerm        # orExpr
    | boolTerm                    # toTerm
    ;

// Expresiones booleanas: AND recursivo
boolTerm
    : boolTerm AND boolFactor     # andExpr
    | boolFactor                  # toFactor
    ;

// Elementos básicos de una expresión booleana:
// permite NOT, paréntesis, variables y valores TRUE/FALSE
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

// Manejo de error lexico cualquier digito sera capturado como un error lexico 
INVALID_NUMBER : [0-9]+ ; // números no permitidos
