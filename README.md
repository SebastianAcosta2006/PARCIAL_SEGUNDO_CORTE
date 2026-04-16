# PARCIAL_SEGUNDO_CORTE
contiene el desarrollo completo del taller de lenguajes de programación, abarcando desde el diseño de gramáticas NoSQL hasta la implementación de algoritmos de análisis sintáctico manuales y automáticos.
Estructura del Proyecto
├── punto1y2/
│   ├── gramatica/   
                     │   ├── NoSQL.g4
                     │   ├── NoSQL.interp
                     │   ├── NoSQL.tokens
                     │   ├── NoSQLLexer.interp
                     │   ├── NoSQLLexer.py
                     │   ├── NoSQLLexer.tokens
                     │   ├── NoSQLListener.py
                     │   ├── NoSQLParser.py
                     │   ├── NoSQL.Vistior.py
│   ├── NoSQL_BNF.txt        
│   ├── entrada.txt         
│   ├── main.py              
│   └── visitor_NoSQL.py     
│
├── punto3/
│   └── gramatica_corregida3.txt 
│
├── punto4/
│   ├── antlr4/
│   │   ├── gramatica/      
                       │   ├── izq.g4
                       │   ├── izq.interp
                       │   ├── izq.tokens
                       │   ├── izqLexer.interp
                       │   ├── izqLexer.py
                       │   ├── izqLexer.tokens
                       │   ├── izqListener.py
                       │   ├── izqParser.py
                       │   ├── izqVisitor.py
│   │   ├── main.py         
│   │   └── visitorIN.py    
│   ├── algoritmocyk.py      
│   ├── comparacionesgrama.py 
│   └── entrada.txt          
│
└── punto5/
    ├── entrada.txt          
    ├── punto5.py            
    └── README.md     
    
Requisitos y Ejecucion (Ubuntu)Instalacion de dependencias:
Bashpip install antlr4-python3-runtime matplotlib numpy
    
Detalle de Implementacion de todos los puntos

punto 1 y 2: el trabajo se centró en el diseño y la implementación técnica de una gramática específica para consultas NoSQL utilizando la herramienta ANTLR4. Inicialmente, se definió la estructura formal del lenguaje en formato BNF, estableciendo las reglas para el reconocimiento de operaciones de bases de datos no relacionales. Posteriormente, se generaron los componentes del analizador (Lexer y Parser) en Python, lo que permitió validar sintácticamente diversas instrucciones de entrada. Finalmente, se implementó un Visitor personalizado para recorrer el árbol sintáctico y procesar la lógica de las consultas, asegurando que el sistema no solo reconociera la estructura del lenguaje, sino que también fuera capaz de interpretar y ejecutar las acciones definidas en los archivos de prueba.

punto 3:el enfoque principal fue la identificación y resolución de la ambigüedad en las gramáticas proporcionadas. Se analizó específicamente el problema del "dangling else" (else suelto), donde una sentencia condicional anidada puede generar dos interpretaciones sintácticas distintas para una misma entrada. Para corregir esto, se aplicó una reestructuración de las reglas gramaticales, diferenciando entre proposiciones "emparejadas" y "no emparejadas". Este proceso garantizó que cada else se asocie de manera unívoca al if más cercano, eliminando la multiplicidad de árboles sintácticos y asegurando que la gramática sea determinista y apta para un parser descendente.
<img width="710" height="416" alt="image" src="https://github.com/user-attachments/assets/149d5b39-4afc-478e-9bba-e6aa3c2ed1ae" />

<img width="689" height="407" alt="image" src="https://github.com/user-attachments/assets/e006c830-bcbe-4ee9-8fbb-98c8c11e288c" />


Punto 4: Análisis de Rendimiento (ANTLR vs. CYK)Enfoque: Comparar un parser $LALR/ALL(*)$ generado automáticamente frente a la ejecución dinámica del algoritmo CYK.Resultado: El script comparacionesgrama.py mide el tiempo de respuesta y genera un reporte visual (reporte_rendimiento.png) que demuestra la eficiencia lineal de ANTLR frente a la complejidad cúbica de CYK.
Bashpython3 punto4/comparacionesgrama.py punto4/entrada.txt
Para el Punto 4, realizamos un análisis comparativo de rendimiento entre dos metodologías de parseo: una automatizada mediante ANTLR4 y otra manual utilizando el algoritmo CYK. El objetivo fue medir cómo escala el tiempo de procesamiento a medida que aumenta la longitud de la cadena de entrada (el número de tokens). A través de un script de benchmark, confirmamos experimentalmente que ANTLR4 opera con una eficiencia casi lineal ($O(n)$), manteniendo tiempos constantes y bajos, mientras que el algoritmo CYK, debido a su naturaleza de programación dinámica, presenta un crecimiento cúbico ($O(n^3)$). Esta diferencia quedó plasmada en una gráfica de rendimiento donde se observa que, ante entradas extensas, el costo computacional de CYK se dispara, validando por qué los parsers predictivos modernos son la opción estándar en el desarrollo de compiladores reales.
<img width="1339" height="730" alt="image" src="https://github.com/user-attachments/assets/d3453937-b86d-41ec-b0dc-68c3c1675339" />


(Punto 5):Bashpython3 punto5/punto5.py punto5/entrada.txt
Punto 5: Algoritmo de Emparejamiento ManualConcepto: Implementación de un Descendente Recursivo utilizando la técnica de consumo de tokens (match).Gramática: Soporta sentencias de asignación (id = num) y condicionales (if cond then asig).

Conclusión:El desarrollo de este taller permitió contrastar las dos vertientes del análisis sintáctico: la automatización y la implementación manual. Mientras que herramientas como ANTLR4 demostraron una eficiencia superior y escalabilidad lineal ($O(n)$) ideal para lenguajes complejos, la implementación manual de algoritmos como CYK y el Descendente Recursivo permitió profundizar en la mecánica interna del reconocimiento de lenguajes, la gestión de la ambigüedad y el costo computacional cúbico ($O(n^3)$) que implican ciertos métodos de programación dinámica. En última instancia, se validó que la correcta estructuración de las gramáticas (evitando recursividad por la izquierda y ambigüedad) es el pilar fundamental para el éxito de cualquier compilador o intérprete.
