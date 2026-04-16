import re

class DescendenteRecursivo:
    def __init__(self, texto):
        self.tokens = re.findall(r'[a-zA-Z]+|[0-9]+|==|=|[;]', texto)
        self.pos = 0
        self.token_actual = self.tokens[self.pos] if self.tokens else None
        print(f"Tokens detectados: {self.tokens}")

    def error(self, esperado):
        raise SyntaxError(f"Error: se esperaba '{esperado}' pero se encontró '{self.token_actual}'")

    def match(self, esperado):
        if self.token_actual == esperado:
            self.pos += 1
            if self.pos < len(self.tokens):
                self.token_actual = self.tokens[self.pos]
            else:
                self.token_actual = None
        else:
            self.error(esperado)
#reglas
    def parsear(self):
        """Punto de entrada: decide si es asignación o condicional"""
        if self.token_actual == "if":
            self.condicional()
        else:
            self.asignacion()
        
        if self.token_actual is None:
            print("✅ ¡La cadena es válida!")
        else:
            print(f"❌ Error: tokens sobrantes al final: {self.token_actual}")

    def asignacion(self):
        """Regla: id = numero"""
        print(f"Procesando Asignación...")
        if str(self.token_actual).isalpha():
            self.pos += 1 # Consumimos el ID manualmente o con lógica extra
            self.token_actual = self.tokens[self.pos] if self.pos < len(self.tokens) else None
            self.match("=")
          
            if str(self.token_actual).isdigit():
                self.match(self.token_actual)
            else:
                self.error("número")
        else:
            self.error("identificador")

    def condicional(self):
        """Regla: if id == numero then Asignacion"""
        print(f"Procesando Condicional...")
        self.match("if")
        
        if str(self.token_actual).isalpha():
            self.pos += 1
            self.token_actual = self.tokens[self.pos] if self.pos < len(self.tokens) else None
        else: self.error("identificador")
        
        self.match("==")
        
        if str(self.token_actual).isdigit():
            self.match(self.token_actual)
        else: self.error("número")
        
        self.match("then")
        self.asignacion()

if __name__ == "__main__":
    print("--- Prueba 1: Asignación ---")
    p1 = DescendenteRecursivo("x = 10")
    p1.parsear()

    print("\n--- Prueba 2: Condicional ---")
    p2 = DescendenteRecursivo("if y == 5 then z = 100")
    p2.parsear()

    print("\n--- Prueba 3: Error ---")
    try:
        p3 = DescendenteRecursivo("if x = 10") 
        p3.parsear()
    except SyntaxError as e:
        print(e)
