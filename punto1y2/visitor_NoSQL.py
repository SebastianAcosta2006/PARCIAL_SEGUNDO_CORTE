# Importamos las clases generadas por tu gramática
from GRAMATICA.NoSQLParser import NoSQLParser
from GRAMATICA.NoSQLVisitor import NoSQLVisitor

class VisitorNoSQL(NoSQLVisitor):
    """
    Esta clase implementa el Punto 2 del taller. 
    Define qué hace el lenguaje cuando encuentra cada operación CRUD.
    """

    def __init__(self):
        # Simulamos una base de datos simple con un diccionario
        self.base_de_datos = {}

    # Visitamos la regla inicial
    def visitInicio(self, ctx: NoSQLParser.InicioContext):
        print("--- [MOTOR NOSQL ACTIVADO] ---")
        return self.visitChildren(ctx)

    # Implementación de AGREGAR (Create)
    def visitCmd_insertar(self, ctx: NoSQLParser.Cmd_insertarContext):
        # id_entidad es la colección (ej: 'estudiantes')
        coleccion = ctx.id_entidad().getText()
        # estructura_datos contiene los campos -> valores
        datos = ctx.estructura_datos().getText()
        
        print(f"[INSERT] Añadiendo registro a la colección '{coleccion}': {datos}")
        
        # Lógica simulada: Guardamos en nuestro diccionario
        if coleccion not in self.base_de_datos:
            self.base_de_datos[coleccion] = []
        self.base_de_datos[coleccion].append(datos)
        
        return None

    # Implementación de OBTENER (Read)
    def visitCmd_buscar(self, ctx: NoSQLParser.Cmd_buscarContext):
        # Revisamos si pide TODO o campos específicos
        seleccion = ctx.seleccion_campos().getText()
        
        print(f"[SELECT] Consultando datos. Criterio: {seleccion}")
        
        if not self.base_de_datos:
            print("   Resultado: La base de datos está vacía.")
        else:
            for col, registros in self.base_de_datos.items():
                print(f"   Colección '{col}': {registros}")
        
        return None

    # Implementación de CAMBIAR (Update)
    def visitCmd_modificar(self, ctx: NoSQLParser.Cmd_modificarContext):
        coleccion = ctx.id_entidad().getText()
        nuevos_datos = ctx.estructura_datos().getText()
        
        print(f"[UPDATE] Modificando colección '{coleccion}' con nuevos valores: {nuevos_datos}")
        
        if coleccion in self.base_de_datos:
            # En una implementación real buscaríamos por ID, aquí actualizamos la referencia
            self.base_de_datos[coleccion] = [nuevos_datos]
        else:
            print(f"   Error: No se encontró la colección '{coleccion}'")
            
        return None

    # Implementación de QUITAR (Delete)
    def visitCmd_remover(self, ctx: NoSQLParser.Cmd_removerContext):
        # En tu gramática, seleccion_campos aquí actúa como el filtro de ID
        identificador = ctx.seleccion_campos().getText()
        
        print(f"[DELETE] Eliminando registro con ID/Criterio: {identificador}")
        
        # Lógica de eliminación simulada
        encontrado = False
        for col in list(self.base_de_datos.keys()):
            if identificador in str(self.base_de_datos[col]):
                del self.base_de_datos[col]
                encontrado = True
        
        if not encontrado:
            print(f"   Aviso: No se realizó ninguna eliminación para: {identificador}")
            
        return None