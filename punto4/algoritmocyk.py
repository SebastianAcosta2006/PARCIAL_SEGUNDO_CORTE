def tokenizar_cyk(linea):

    tokens = []
    i = 0
    linea = linea.replace(" ", "")
    while i < len(linea):
        if linea[i].isdigit():
        
            while i < len(linea) and (linea[i].isdigit() or linea[i] == '.'):
                i += 1
            tokens.append("num")
            continue
        else:
            tokens.append(linea[i])
        i += 1
    return tokens

def parsear_cyk(tokens):
    """ implementacion del algoritmocyk para verificar si la cadena pertenece a la gramatica de la calculadora
    """
    n = len(tokens)
    if n == 0: return False

    gramatica = {
        "S": [("N", "OpN"), "num"],
        "OpN": [("Op", "N")],
        "N": ["num"],
        "Op": ["+", "-", "*", "/"]
    }

    tabla = [[set() for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for nt, producciones in gramatica.items():
            if tokens[i] in producciones:
                tabla[i][i].add(nt)

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
    try:
      
        expresion = "".join(tokens_originales)
        return float(eval(expresion))
    except:
        return None
