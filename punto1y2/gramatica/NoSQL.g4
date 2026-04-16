grammar NoSQL;

// Punto de entrada: ahora el archivo se compone de diversas operaciones
inicio : operacion+ EOF ;

operacion
    : cmd_insertar
    | cmd_buscar
    | cmd_modificar
    | cmd_remover
    ;

// Estructura cambiada: COMANDO(coleccion, {datos})
cmd_insertar  : 'AGREGAR' '(' id_entidad ',' estructura_datos ')' ';' ;
cmd_buscar    : 'OBTENER' '(' seleccion_campos ')' ';' ;
cmd_modificar : 'CAMBIAR' '(' id_entidad ',' estructura_datos ')' ';' ;
cmd_remover   : 'QUITAR' '(' seleccion_campos ')' ';' ;

// Manejo de proyecciones o filtros
seleccion_campos
    : TODO
    | id_entidad (',' id_entidad)*
    ;

// Definición de la estructura de un documento NoSQL
estructura_datos
    : '{' asignacion (',' asignacion)* '}'
    | '{' '}' 
    ;

asignacion
    : id_entidad '->' dato
    ;

dato
    : VAL_NUMERO
    | VAL_TEXTO
    | id_entidad
    | coleccion_datos
    | estructura_datos
    ;

coleccion_datos
    : '<' dato (',' dato)* '>'
    | '<' '>'
    ;

id_entidad : IDENTIFICADOR ;

// --- BLOQUE LÉXICO (Tokens) ---

// Palabras clave con soporte para mayúsculas/minúsculas mediante fragmentos
AGREGAR   : A G R E G A R ;
OBTENER   : O B T E N E R ;
CAMBIAR   : C A M B I A R ;
QUITAR    : Q U I T A R ;
TODO      : T O D O ;

// Tipos de datos
VAL_NUMERO : '-'? [0-9]+ ('.' [0-9]+)? ;
VAL_TEXTO  : '"' (~["\r\n])* '"' ;
IDENTIFICADOR : [a-zA-Z_][a-zA-Z0-9_]* ;

// Ignorar espacios y saltos
ESPACIOS : [ \t\r\n]+ -> skip ;

// Fragmentos para Case Insensitivity
fragment A:[aA]; fragment B:[bB]; fragment C:[cC]; fragment D:[dD];
fragment E:[eE]; fragment F:[fF]; fragment G:[gG]; fragment H:[hH];
fragment I:[iI]; fragment J:[jJ]; fragment K:[kK]; fragment L:[lL];
fragment M:[mM]; fragment N:[nN]; fragment O:[oO]; fragment P:[pP];
fragment Q:[qQ]; fragment R:[rR]; fragment S:[sS]; fragment T:[tT];
fragment U:[uU]; fragment V:[vV]; fragment W:[wW]; fragment X:[xX];
fragment Y:[yY]; fragment Z:[zZ];
