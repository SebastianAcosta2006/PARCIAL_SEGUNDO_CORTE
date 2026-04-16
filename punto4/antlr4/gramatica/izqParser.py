# Generated from izqNormal.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

def serializedATN():
    return [
        4,1,6,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,3,1,3,1,3,
        1,3,1,3,3,3,45,8,3,1,3,0,2,2,4,4,0,2,4,6,0,2,1,0,1,2,1,0,3,4,51,
        0,7,1,0,0,0,2,10,1,0,0,0,4,28,1,0,0,0,6,44,1,0,0,0,8,9,5,2,0,0,9,
        1,1,0,0,0,10,11,6,1,-1,0,11,12,5,4,0,0,12,24,1,0,0,0,13,14,10,4,
        0,0,14,15,7,0,0,0,15,23,5,4,0,0,16,17,10,3,0,0,17,18,7,0,0,0,18,
        23,5,4,0,0,19,20,10,1,0,0,20,21,5,2,0,0,21,23,5,4,0,0,22,13,1,0,
        0,0,22,16,1,0,0,0,22,19,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,
        1,0,0,0,25,3,1,0,0,0,26,24,1,0,0,0,27,28,6,2,-1,0,28,29,5,6,0,0,
        29,36,1,0,0,0,30,31,10,3,0,0,31,32,7,1,0,0,32,35,5,6,0,0,33,35,10,
        2,0,0,34,30,1,0,0,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,
        37,1,0,0,0,37,5,1,0,0,0,38,36,1,0,0,0,39,45,5,5,0,0,40,41,5,7,0,
        0,41,42,5,2,0,0,42,43,5,8,0,0,43,45,1,0,0,0,44,39,1,0,0,0,44,40,
        1,0,0,0,45,7,1,0,0,0,5,22,24,34,36,44
    ]

class izqNormalParser ( Parser ):
    atn = ATNDeserializer().deserialize(serializedATN())
    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]
    sharedContextCache = PredictionContextCache()

    OP_SUMA=1; OP_RESTA=2; OP_MULT=3; OP_DIV=4; VAL_NUMERO=5; ESPACIOS=6

    ruleNames = [ "inicio", "calculo", "producto", "valor_base" ]

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    # ... (Se omiten métodos internos de reglas por brevedad, pero esta es la estructura base necesaria)