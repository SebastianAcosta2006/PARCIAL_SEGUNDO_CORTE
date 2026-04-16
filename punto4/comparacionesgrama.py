import sys
import os
import time
import matplotlib.pyplot as plt
import numpy as np

# configuracion de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "GRAMATICA"))

from visitorIN import VisitorCalculadora
from GRAMATICA.izqLexer import izqLexer
from GRAMATICA.izqParser import izqParser
from antlr4 import *
from cyk import algoritmo_cyk, gramatica_cnf

class AnalizadorRendimiento:
    def __init__(self):
        self.datos = {
            "longitud": [],
            "t_antlr": [],
            "t_cyk": [],
            "match": []
        }

    def medir_antlr(self, linea):
        inicio = time.perf_counter()
        input_stream = InputStream(linea)
        lexer = izqLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = izqParser(stream)
        parser.removeErrorListeners()
        tree = parser.inicio()
        
        resultado = None
        if parser.getNumberOfSyntaxErrors() == 0:
            try:
                visitor = VisitorCalculadora()
                resultado = visitor.visit(tree)
            except: pass
            
        return time.perf_counter() - inicio, resultado

    def medir_cyk(self, linea):
    
        tokens = []
        for char in linea.replace(" ", ""):
            if char.isdigit():
                if not tokens or tokens[-1] != "num": tokens.append("num")
            else: tokens.append(char)
        
        inicio = time.perf_counter()
        es_valida = algoritmo_cyk(tokens, gramatica_cnf)
        duracion = time.perf_counter() - inicio
        
        return duracion, es_valida

    def generar_grafica(self):
        plt.style.use('ggplot')
        fig, ax = plt.subplots(figsize=(10, 6))
        
        x = np.arange(len(self.datos["longitud"]))
        width = 0.35

        ax.bar(x - width/2, self.datos["t_antlr"], width, label='ANTLR (Predictivo)', color='#3498db')
        ax.bar(x + width/2, self.datos["t_cyk"], width, label='CYK (Manual)', color='#e74c3c')

        ax.set_xlabel('Índice de Prueba (Carga de Trabajo)')
        ax.set_ylabel('Tiempo de Ejecución (segundos)')
        ax.set_title('Análisis de Complejidad: ANTLR vs CYK')
        ax.set_xticks(x)
        ax.set_xticklabels([f"L:{l}" for l in self.datos["longitud"]])
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

        plt.savefig('reporte_rendimiento.png', dpi=300)
        print("\n[INFO] Gráfica de barras guardada como 'reporte_rendimiento.png'")

def ejecutar_benchmark():
    if len(sys.argv) < 2:
        print("Error: Se requiere un archivo de entrada (ej: python3 comparacion.py entrada.txt)")
        return

    analizador = AnalizadorRendimiento()
    
    try:
        with open(sys.argv[1], 'r') as f:
            lineas = [l.strip() for l in f if l.strip()]

        print(f"\n{'#' :<3} | {'TIEMPO ANTLR':<15} | {'TIEMPO CYK':<15} | {'ESTADO'}")
        print("-" * 60)

        for i, linea in enumerate(lineas):
            t_a, res_a = analizador.medir_antlr(linea)
            t_c, ok_c = analizador.medir_cyk(linea)
            
            analizador.datos["longitud"].append(len(linea.replace(" ","")))
            analizador.datos["t_antlr"].append(t_a)
            analizador.datos["t_cyk"].append(t_c)
            
            estado = "OK" if (res_a is not None and ok_c) else "DIFF"
            print(f"{i+1:<3} | {t_a:14.6f}s | {t_c:14.6f}s | {estado}")

        analizador.generar_grafica()
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo de entrada.")

if __name__ == "__main__":
    ejecutar_benchmark()
