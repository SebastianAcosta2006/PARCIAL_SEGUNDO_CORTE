import sys
import os
from antlr4 import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from GRAMATICA.NoSQLLexer import NoSQLLexer
from GRAMATICA.NoSQLParser import NoSQLParser
from PUNTOS_1_2.visitor_NoSQL import VisitorNoSQL

class MotorNoSQL:
    """Clase encargada del analisis"""
    
    def __init__(self):
        self.visitor = VisitorNoSQL()

    def procesar_codigo(self, texto_fuente):
        try:
            #lexico
            stream = InputStream(texto_fuente)
            analizador_lexico = NoSQLLexer(stream)
            flujo_tokens = CommonTokenStream(analizador_lexico)
            
            #sintactico
            analizador_sintactico = NoSQLParser(flujo_tokens)
            arbol_sintactico = analizador_sintactico.inicio() 

            #visitor par ajecutar
            print("--- Iniciando Ejecución del Script NoSQL ---")
            self.visitor.visit(arbol_sintactico)
            print("--- Ejecución finalizada con éxito ---")
            
        except Exception as e:
            print(f"Error crítico durante el procesamiento: {e}")

def principal():
    if len(sys.argv) < 2:
        print("Uso: python main_ejecutor.py <archivo_con_instrucciones.nosql>")
        return

    ruta_archivo = sys.argv[1]
    
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo '{ruta_archivo}' no existe en el sistema.")
        return
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            
        motor = MotorNoSQL()
        motor.procesar_codigo(contenido)
        
    except IOError as e:
        print(f"Error al leer el archivo: {e}")

if __name__ == "__main__":
    principal()
