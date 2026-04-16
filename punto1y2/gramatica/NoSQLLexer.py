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
        4,0,18,250,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,
        2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,
        9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,
        15,1,16,1,16,1,17,1,17,0,0,18,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,
        17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,0,0,250
    ]

class NoSQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    # Tokens de puntuacion y operadores
    T__0 = 1 # ,
    T__1 = 2 # ;
    T__2 = 3 # (
    T__3 = 4 # )
    T__4 = 5 # {
    T__5 = 6 # }
    T__6 = 7 # ->
    T__7 = 8 # <
    T__8 = 9 # >

    # crude en españoll
    AGREGAR = 10
    OBTENER = 11
    CAMBIAR = 12
    QUITAR = 13
    TODO = 14

    # yipos de datos
    VAL_NUMERO = 15
    VAL_TEXTO = 16
    IDENTIFICADOR = 17
    ESPACIOS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "'('", "')'", "'{'", "'}'", "'->'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "AGREGAR", "OBTENER", "CAMBIAR", "QUITAR", "TODO", 
            "VAL_NUMERO", "VAL_TEXTO", "IDENTIFICADOR", "ESPACIOS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8",
                  "AGREGAR", "OBTENER", "CAMBIAR", "QUITAR", "TODO", 
                  "VAL_NUMERO", "VAL_TEXTO", "IDENTIFICADOR", "ESPACIOS",
                  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

    grammarFileName = "NoSQL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
