grammar izq;

// regla inicial
inicio : calculo EOF ;

// maneja sumas y restas
calculo
    : calculo OP_SUMA producto
    | calculo OP_RESTA producto
    | producto
    | OP_RESTA producto // Para números negativos al inicio
    ;

// maneja multiplicaciones y divisiones
producto
    : producto OP_MULT valor_base
    | producto OP_DIV valor_base
    | valor_base
    ;

// numeros o expresiones entre parentesis
valor_base
    : VAL_NUMERO
    | '(' calculo ')'
    ;

// definicion de Lexer Tokens
OP_SUMA  : '+' ;
OP_RESTA : '-' ;
OP_MULT  : '*' ;
OP_DIV   : '/' ;

VAL_NUMERO : [0-9]+ ('.' [0-9]+)? ;

// ignorar espacios y saltos de linea
ESPACIOS : [ \t\r\n]+ -> skip ;
