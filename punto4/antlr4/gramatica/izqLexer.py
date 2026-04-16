# Generated from izq.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,1,6,44,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,4,4,25,8,4,11,4,12,4,26,1,4,
        1,4,4,4,31,8,4,11,4,12,4,32,3,4,35,8,4,1,5,4,5,38,8,5,11,5,12,5,
        39,1,5,1,5,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,41,7,43,1,0,3,
        1,0,43,43,1,0,42,42,1,0,45,45,1,0,47,47,3,0,9,10,13,13,32,32,48,
        47,0,1,1,0,0,0,3,1,0,0,0,5,1,0,0,0,7,1,0,0,0,9,1,0,0,0,11,1,0,0,
        0,41,1,0,0,0,13,14,7,0,0,0,14,2,1,0,0,0,15,16,7,1,0,0,16,4,1,0,0,
        0,17,18,7,2,0,0,18,6,1,0,0,0,19,20,7,3,0,0,20,8,1,0,0,0,24,25,3,
        13,6,0,25,24,1,0,0,0,25,26,1,0,0,0,26,34,1,0,0,0,27,28,10,46,0,0,
        28,30,3,13,6,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,
        0,0,0,32,35,1,0,0,0,33,35,1,0,0,0,34,27,1,0,0,0,34,33,1,0,0,0,35,
        10,1,0,0,0,37,38,7,4,0,0,38,37,1,0,0,0,38,39,1,0,0,0,39,40,1,0,0,
        0,40,42,6,5,0,0,41,12,1,0,0,0,42,43,7,5,0,0,43,14,1,0,0,0,5,0,25,
        31,34,38,1,6,0,0
    ]

class izqLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OP_SUMA = 1
    OP_RESTA = 2
    OP_MULT = 3
    OP_DIV = 4
    VAL_NUMERO = 5
    ESPACIOS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "OP_SUMA", "OP_RESTA", "OP_MULT", "OP_DIV", 
                      "VAL_NUMERO", "ESPACIOS" ]

    ruleNames = [ "OP_SUMA", "OP_RESTA", "OP_MULT", "OP_DIV", "VAL_NUMERO", 
                  "ESPACIOS", "DIGITO" ]

    grammarFileName = "izq.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
