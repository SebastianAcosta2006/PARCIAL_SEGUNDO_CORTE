# Generated from izqNormal.g4 by ANTLR 4.13.2
from antlr4 import *
if __name__ == "__main__":
    import izqNormalParser
else:
    from .izqNormalParser import izqNormalParser

class izqNormalListener(ParseTreeListener):
    def enterInicio(self, ctx:izqNormalParser.InicioContext): pass
    def exitInicio(self, ctx:izqNormalParser.InicioContext): pass

    def enterCalculo(self, ctx:izqNormalParser.CalculoContext): pass
    def exitCalculo(self, ctx:izqNormalParser.CalculoContext): pass

    def enterProducto(self, ctx:izqNormalParser.ProductoContext): pass
    def exitProducto(self, ctx:izqNormalParser.ProductoContext): pass

    def enterValor_base(self, ctx:izqNormalParser.Valor_baseContext): pass
    def exitValor_base(self, ctx:izqNormalParser.Valor_baseContext): pass