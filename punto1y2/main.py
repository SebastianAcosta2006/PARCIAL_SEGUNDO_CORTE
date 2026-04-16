import sys
import os
from antlr4 import *

# Ajuste de paths para encontrar tus módulos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Importaciones con los nombres en español que definimos
from GRAMATICA.NoSQLLexer import NoSQLLexer
from GRAMATICA.NoSQLParser import NoSQLParser
from PUNTOS_1_2.visitor_NoSQL import VisitorNoSQL

class MotorNoSQL:
    """Clase encargada de orquestar el análisis y ejecución del lenguaje."""
    
    def __init__(self):
        self.visitor = VisitorNoSQL()

    def procesar_codigo(self, texto_fuente):
        try:
            # 1. Análisis Léxico
            stream = InputStream(texto_fuente)
            analizador_lexico = NoSQLLexer(stream)
            flujo_tokens = CommonTokenStream(analizador_lexico)
            
            # 2. Análisis Sintáctico
            analizador_sintactico = NoSQLParser(flujo_tokens)
            # Cambiamos 'programa' por 'inicio' que es el nombre de tu regla principal
            arbol_sintactico = analizador_sintactico.inicio() 

            # 3. Ejecución vía Visitor
            print("--- Iniciando Ejecución del Script NoSQL ---")
            self.visitor.visit(arbol_sintactico)
            print("--- Ejecución finalizada con éxito ---")
            
        except Exception as e:
            print(f"Error crítico durante el procesamiento: {e}")

def principal():
    # Verificación de parámetros de entrada
    if len(sys.argv) < 2:
        print("Uso: python main_ejecutor.py <archivo_con_instrucciones.nosql>")
        return

    ruta_archivo = sys.argv[1]
    
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo '{ruta_archivo}' no existe en el sistema.")
        return

    # Lectura y ejecución
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            
        motor = MotorNoSQL()
        motor.procesar_codigo(contenido)
        
    except IOError as e:
        print(f"Error al leer el archivo: {e}")

if __name__ == "__main__":
    principal()