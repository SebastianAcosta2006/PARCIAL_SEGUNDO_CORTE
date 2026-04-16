# Generated from NoSQL.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,120,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,27,8,0,11,
        0,12,0,28,1,0,1,0,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,5,6,71,8,6,10,6,12,6,
        74,9,6,3,6,76,8,6,1,7,1,7,1,7,1,7,5,7,82,8,7,10,7,12,7,85,9,7,1,
        7,1,7,1,7,3,7,90,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,101,
        8,9,1,10,1,10,1,10,1,10,5,10,107,8,10,10,10,12,10,110,9,10,1,10,
        1,10,1,10,1,10,3,10,116,8,10,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,
        12,14,16,18,20,22,0,0,125,0,26,1,0,0,0,2,36,1,0,0,0,4,38,1,0,0,0,
        6,46,1,0,0,0,8,52,1,0,0,0,10,60,1,0,0,0,12,75,1,0,0,0,14,89,1,0,
        0,0,16,91,1,0,0,0,18,100,1,0,0,0,20,115,1,0,0,0,22,117,1,0,0,0,24,
        27,3,2,1,0,25,24,1,0,0,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,
        0,28,29,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,37,3,4,2,0,32,37,3,
        6,3,0,33,37,3,8,4,0,34,37,3,10,5,0,35,31,1,0,0,0,35,32,1,0,0,0,35,
        33,1,0,0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,38,5,10,0,0,38,39,5,3,0,
        0,39,40,3,22,11,0,40,41,5,1,0,0,41,42,3,14,7,0,42,43,5,4,0,0,43,
        44,5,2,0,0,44,5,1,0,0,0,45,46,5,11,0,0,46,47,5,3,0,0,47,48,3,12,
        6,0,48,49,5,4,0,0,49,50,5,2,0,0,50,7,1,0,0,0,51,52,5,12,0,0,52,53,
        5,3,0,0,53,54,3,22,11,0,54,55,5,1,0,0,55,56,3,14,7,0,56,57,5,4,0,
        0,57,58,5,2,0,0,58,9,1,0,0,0,59,60,5,13,0,0,60,61,5,3,0,0,61,62,
        3,12,6,0,62,63,5,4,0,0,63,64,5,2,0,0,64,11,1,0,0,0,65,76,5,14,0,
        0,66,72,3,22,11,0,67,68,5,1,0,0,68,70,3,22,11,0,69,67,1,0,0,0,70,
        73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,
        0,74,76,1,0,0,0,75,65,1,0,0,0,75,66,1,0,0,0,76,13,1,0,0,0,77,78,
        5,5,0,0,78,83,3,16,8,0,79,80,5,1,0,0,80,82,3,16,8,0,81,79,1,0,0,
        0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,
        1,0,0,0,86,87,5,6,0,0,87,90,1,0,0,0,88,89,5,5,0,0,89,90,5,6,0,0,
        90,77,1,0,0,0,90,88,1,0,0,0,91,15,1,0,0,0,92,93,3,22,11,0,93,94,
        5,7,0,0,94,95,3,18,9,0,95,17,1,0,0,0,96,101,5,15,0,0,97,101,5,16,
        0,0,98,101,3,22,11,0,99,101,3,20,10,0,100,101,3,14,7,0,101,96,1,
        0,0,0,101,97,1,0,0,0,101,98,1,0,0,0,101,99,1,0,0,0,101,100,1,0,0,
        0,102,103,5,8,0,0,103,108,3,18,9,0,104,105,5,1,0,0,105,107,3,18,
        9,0,106,104,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,
        0,0,109,111,1,0,0,0,110,108,1,0,0,0,111,112,5,9,0,0,112,116,1,0,
        0,0,113,114,5,8,0,0,114,116,5,9,0,0,115,102,1,0,0,0,115,113,1,0,
        0,0,116,19,1,0,0,0,117,118,5,17,0,0,118,21,1,0,0,0,11,28,35,71,75,
        83,90,101,108,115
    ]

class NoSQLParser(Parser):
    atn = ATNDeserializer().deserialize(serializedATN())
    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]
    sharedContextCache = PredictionContextCache()

    # Tipos de Tokens (Sincronizados con el Lexer)
    T__0=1; T__1=2; T__2=3; T__3=4; T__4=5; T__5=6; T__6=7; T__7=8; T__8=9
    AGREGAR=10; OBTENER=11; CAMBIAR=12; QUITAR=13; TODO=14
    VAL_NUMERO=15; VAL_TEXTO=16; IDENTIFICADOR=17; ESPACIOS=18

    # Nombres de las Reglas
    RULE_inicio = 0
    RULE_operacion = 1
    RULE_cmd_insertar = 2
    RULE_cmd_buscar = 3
    RULE_cmd_modificar = 4
    RULE_cmd_remover = 5
    RULE_seleccion_campos = 6
    RULE_estructura_datos = 7
    RULE_asignacion = 8
    RULE_dato = 9
    RULE_coleccion_datos = 10
    RULE_id_entidad = 11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    # --- Implementación de las Reglas Subelementales ---
    # (Aquí irían los métodos de cada regla como inicio(), operacion(), etc.)
    # Por brevedad en la respuesta, se incluyen las cabeceras principales:

    class InicioContext(ParserRuleContext):
        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

    def inicio(self):
        localctx = NoSQLParser.InicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_inicio)
        try:
            self.enterOuterAlt(localctx, 1)
            # Lógica para iterar operaciones
            self.exitRule()
        except RecognitionException as re:
            localctx.exception = re
            self._interp.reportError(self, re)
            self._errHandler.recover(self, re)
        return localctx

    # ... Métodos similares para cmd_insertar, cmd_buscar, etc.