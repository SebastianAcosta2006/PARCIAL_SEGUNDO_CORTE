# Generated from izq.g4 by ANTLR 4.13.2
from antlr4 import *
if __name__ == "__main__":
    import izqParser
else:
    from .izqParser import izqParser

class izqVisitor(ParseTreeVisitor):
    def visitInicio(self, ctx:izqParser.InicioContext):
        return self.visitChildren(ctx)

    def visitCalculo(self, ctx:izqParser.CalculoContext):
        return self.visitChildren(ctx)

    def visitProducto(self, ctx:izqParser.ProductoContext):
        return self.visitChildren(ctx)

    def visitValor_base(self, ctx:izqParser.Valor_baseContext):
        return self.visitChildren(ctx)
