grammar izqNormal;

// Regla inicial
inicio : calculo EOF ;

// Maneja sumas y restas (Menor precedencia)
calculo
    : calculo OP_SUMA producto
    | calculo OP_RESTA producto
    | producto
    | OP_RESTA producto // Para números negativos al inicio
    ;

// Maneja multiplicaciones y divisiones
producto
    : producto OP_MULT valor_base
    | producto OP_DIV valor_base
    | valor_base
    ;

// El corazón de la recursividad: números o expresiones entre paréntesis
valor_base
    : VAL_NUMERO
    | '(' calculo ')'
    ;

// Definición de Lexer (Tokens)
OP_SUMA  : '+' ;
OP_RESTA : '-' ;
OP_MULT  : '*' ;
OP_DIV   : '/' ;

VAL_NUMERO : [0-9]+ ('.' [0-9]+)? ;

// Ignorar espacios y saltos de línea
ESPACIOS : [ \t\r\n]+ -> skip ;
