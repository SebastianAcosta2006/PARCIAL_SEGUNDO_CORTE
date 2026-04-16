def tokenizar_cyk(linea):
    """
    Convierte una expresión como '10 + 5' en tokens genéricos
    para que el algoritmo CYK los procese (ej: ['num', '+', 'num']).
    """
    tokens = []
    i = 0
    linea = linea.replace(" ", "")
    while i < len(linea):
        if linea[i].isdigit():
            # Agrupar dígitos para formar un solo token 'num'
            while i < len(linea) and (linea[i].isdigit() or linea[i] == '.'):
                i += 1
            tokens.append("num")
            continue
        else:
            tokens.append(linea[i])
        i += 1
    return tokens

def parsear_cyk(tokens):
    """
    Implementación del algoritmo CYK para verificar si la cadena
    pertenece a la gramática de la calculadora en Forma Normal de Chomsky.
    """
    n = len(tokens)
    if n == 0: return False

    # Definición de la Gramática en Forma Normal de Chomsky (CNF)
    # S -> N OpN | num
    # OpN -> Op N
    # Op -> + | - | * | /
    # N -> num
    gramatica = {
        "S": [("N", "OpN"), "num"],
        "OpN": [("Op", "N")],
        "N": ["num"],
        "Op": ["+", "-", "*", "/"]
    }

    # Inicialización de la tabla de programación dinámica
    tabla = [[set() for _ in range(n)] for _ in range(n)]

    # Paso 1: Llenado de la diagonal (Reglas terminales)
    for i in range(n):
        for nt, producciones in gramatica.items():
            if tokens[i] in producciones:
                tabla[i][i].add(nt)

    # Paso 2: Llenado de la tabla (Reglas binarias A -> BC)
    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            for k in range(i, j):
                for nt, producciones in gramatica.items():
                    for p in producciones:
                        if isinstance(p, tuple):
                            B, C = p
                            if B in tabla[i][k] and C in tabla[k+1][j]:
                                tabla[i][j].add(nt)

    return "S" in tabla[0][n-1]

def evaluar_cyk(tokens_originales):
    """
    Simulación de evaluación para el algoritmo CYK.
    Como CYK es solo un reconocedor, usamos eval() de Python 
    sobre los tokens originales para comparar resultados con ANTLR.
    """
    try:
        # Unimos los tokens originales para evaluar la expresión matemática
        expresion = "".join(tokens_originales)
        return float(eval(expresion))
    except:
        return None