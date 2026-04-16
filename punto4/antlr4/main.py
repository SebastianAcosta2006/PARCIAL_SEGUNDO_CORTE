import sys
import os
import time
from antlr4 import *

# configuracion de rutas para importar desde la carpeta gramatica
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'GRAMATICA')))

# importes ajustados a tus nuevos nombres de archivo
from GRAMATICA.izqLexer import izqLexer
from GRAMATICA.izqParser import izqParser
from visitorIN import VisitorCalculadora 

class MotorCalculadora:
    def __init__(self):
        self.visitor = VisitorCalculadora()

    def procesar_linea(self, texto):
        
        t_inicio = time.perf_counter()
        
        input_stream = InputStream(texto)
        lexer = izqLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = izqParser(token_stream)

       
        lexer.removeErrorListeners()
        parser.removeErrorListeners()

        # regla principalde gramaticad
        arbol = parser.inicio()
        t_final = time.perf_counter()
        duracion = t_final - t_inicio

        if parser.getNumberOfSyntaxErrors() == 0:
            try:
                valor = self.visitor.visit(arbol)
                return f"[OK] Res: {valor:.2f}", duracion
            except Exception as e:
                return f"[ERROR EVAL] {str(e)}", duracion
        else:
            return "[RECHAZADA] Sintaxis inválida", duracion

def ejecutar():
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <archivo_entrada.txt>")
        return

    ruta_archivo = sys.argv[1]
    
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        return

    calc = MotorCalculadora()
    print(f"{'EXPRESIÓN':<30} | {'ESTADO/RESULTADO':<25} | {'TIEMPO'}")
    print("-" * 75)

    with open(ruta_archivo, 'r') as f:
        for linea in f:
            clean_line = linea.strip()
            if not clean_line:
                continue
            
            status, crono = calc.procesar_linea(clean_line)
            print(f"{clean_line:<30} | {status:<25} | {crono:.6f}s")

if __name__ == "__main__":
    ejecutar()
