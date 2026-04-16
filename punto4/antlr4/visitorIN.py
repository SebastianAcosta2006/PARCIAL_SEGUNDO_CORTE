import sys
import os

# Aseguramos que Python encuentre los archivos generados por ANTLR
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'GRAMATICA')))

from GRAMATICA.izqVisitor import izqVisitor
from GRAMATICA.izqParser import izqParser

class VisitorCalculadora(izqVisitor):

    # Visita la regla raíz: inicio
    def visitInicio(self, ctx: izqParser.InicioContext):
        return self.visit(ctx.calculo())

    # Maneja la lógica de Suma y Resta (y unarios)
    def visitCalculo(self, ctx: izqParser.CalculoContext):
        # Si es un solo hijo, pasamos al siguiente nivel (producto)
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        # Caso para números negativos iniciales (ej: -5)
        if ctx.getChildCount() == 2 and ctx.OP_RESTA():
            return -self.visit(ctx.producto())

        # Operaciones binarias: calculo OP producto
        # ANTLR estructura esto de forma que el primer hijo es 'calculo' 
        # y el último es 'producto'
        resultado_izq = self.visit(ctx.calculo())
        resultado_der = self.visit(ctx.producto())

        if ctx.OP_SUMA():
            return resultado_izq + resultado_der
        if ctx.OP_RESTA():
            return resultado_izq - resultado_der

    # Maneja la lógica de Multiplicación y División
    def visitProducto(self, ctx: izqParser.ProductoContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.valor_base())

        resultado_izq = self.visit(ctx.producto())
        resultado_der = self.visit(ctx.valor_base())

        if ctx.OP_MULT():
            return resultado_izq * resultado_der
        if ctx.OP_DIV():
            # Manejo básico de error por división entre cero
            denom = resultado_der
            if denom == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            return resultado_izq / denom

    # Maneja números finales y expresiones entre paréntesis
    def visitValor_base(self, ctx: izqParser.Valor_baseContext):
        # Si el token es un número
        if ctx.VAL_NUMERO():
            return float(ctx.VAL_NUMERO().getText())
        
        # Si la expresión está entre paréntesis (calculo)
        # El calculo está en la posición del hijo 1: '(' 'calculo' ')'
        return self.visit(ctx.calculo())