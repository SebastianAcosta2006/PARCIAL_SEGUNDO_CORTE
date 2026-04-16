# Generated from izq.g4 by ANTLR 4.13.2
from antlr4 import *
if __name__ == "__main__":
    import izqParser
else:
    from .izqParser import izqParser

class izqListener(ParseTreeListener):
    def enterInicio(self, ctx:izqParser.InicioContext): pass
    def exitInicio(self, ctx:izqParser.InicioContext): pass

    def enterCalculo(self, ctx:izqParser.CalculoContext): pass
    def exitCalculo(self, ctx:izqParser.CalculoContext): pass

    def enterProducto(self, ctx:izqParser.ProductoContext): pass
    def exitProducto(self, ctx:izqParser.ProductoContext): pass

    def enterValor_base(self, ctx:izqParser.Valor_baseContext): pass
    def exitValor_base(self, ctx:izqParser.Valor_baseContext): pass
