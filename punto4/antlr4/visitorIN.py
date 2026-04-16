import sys
import os

# python encuentra los archivos en atnrl
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'GRAMATICA')))

from GRAMATICA.izqVisitor import izqVisitor
from GRAMATICA.izqParser import izqParser

class VisitorCalculadora(izqVisitor):

    def visitInicio(self, ctx: izqParser.InicioContext):
        return self.visit(ctx.calculo())
 
    def visitCalculo(self, ctx: izqParser.CalculoContext):                 
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

    
        if ctx.getChildCount() == 2 and ctx.OP_RESTA():
            return -self.visit(ctx.producto())
        resultado_izq = self.visit(ctx.calculo())
        resultado_der = self.visit(ctx.producto())

        if ctx.OP_SUMA():
            return resultado_izq + resultado_der
        if ctx.OP_RESTA():
            return resultado_izq - resultado_der

    def visitProducto(self, ctx: izqParser.ProductoContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.valor_base())

        resultado_izq = self.visit(ctx.producto())
        resultado_der = self.visit(ctx.valor_base())

        if ctx.OP_MULT():
            return resultado_izq * resultado_der
        if ctx.OP_DIV():
            denom = resultado_der
            if denom == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            return resultado_izq / denom

    def visitValor_base(self, ctx: izqParser.Valor_baseContext):   
        if ctx.VAL_NUMERO():
            return float(ctx.VAL_NUMERO().getText())
                     
        return self.visit(ctx.calculo())
