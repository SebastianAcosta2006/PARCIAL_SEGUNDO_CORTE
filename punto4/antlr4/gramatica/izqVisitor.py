# Generated from izqNormal.g4 by ANTLR 4.13.2
from antlr4 import *
if __name__ == "__main__":
    import izqNormalParser
else:
    from .izqNormalParser import izqNormalParser

class izqNormalVisitor(ParseTreeVisitor):
    def visitInicio(self, ctx:izqNormalParser.InicioContext):
        return self.visitChildren(ctx)

    def visitCalculo(self, ctx:izqNormalParser.CalculoContext):
        return self.visitChildren(ctx)

    def visitProducto(self, ctx:izqNormalParser.ProductoContext):
        return self.visitChildren(ctx)

    def visitValor_base(self, ctx:izqNormalParser.Valor_baseContext):
        return self.visitChildren(ctx)