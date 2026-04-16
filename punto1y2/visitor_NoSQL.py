# importar clases generadas por la gramatia
from GRAMATICA.NoSQLParser import NoSQLParser
from GRAMATICA.NoSQLVisitor import NoSQLVisitor

class VisitorNoSQL(NoSQLVisitor):
    """
    Esta clase implementa el punto 2
    """

    def __init__(self):
    
        self.base_de_datos = {}
    def visitInicio(self, ctx: NoSQLParser.InicioContext):
        print("--- [MOTOR NOSQL ACTIVADO] ---")
        return self.visitChildren(ctx)

    # agregar
    def visitCmd_insertar(self, ctx: NoSQLParser.Cmd_insertarContext):
        coleccion = ctx.id_entidad().getText()
        datos = ctx.estructura_datos().getText()
        
        print(f"[INSERT] Añadiendo registro a la colección '{coleccion}': {datos}")
        if coleccion not in self.base_de_datos:
            self.base_de_datos[coleccion] = []
        self.base_de_datos[coleccion].append(datos)
        
        return None

    # obtener
    def visitCmd_buscar(self, ctx: NoSQLParser.Cmd_buscarContext):
        seleccion = ctx.seleccion_campos().getText()
        
        print(f"[SELECT] Consultando datos. Criterio: {seleccion}")
        if not self.base_de_datos:
            print("   Resultado: La base de datos está vacía.")
        else:
            for col, registros in self.base_de_datos.items():
                print(f"   Colección '{col}': {registros}")
        
        return None

    # cambiar
    def visitCmd_modificar(self, ctx: NoSQLParser.Cmd_modificarContext):
        coleccion = ctx.id_entidad().getText()
        nuevos_datos = ctx.estructura_datos().getText()
        
        print(f"[UPDATE] Modificando colección '{coleccion}' con nuevos valores: {nuevos_datos}")
        
        if coleccion in self.base_de_datos:
            self.base_de_datos[coleccion] = [nuevos_datos]
        else:
            print(f"   Error: No se encontró la colección '{coleccion}'")
            
        return None

    # quitar
    def visitCmd_remover(self, ctx: NoSQLParser.Cmd_removerContext):
        identificador = ctx.seleccion_campos().getText()
        
        print(f"[DELETE] Eliminando registro con ID/Criterio: {identificador}")
        
        encontrado = False
        for col in list(self.base_de_datos.keys()):
            if identificador in str(self.base_de_datos[col]):
                del self.base_de_datos[col]
                encontrado = True
        
        if not encontrado:
            print(f"   Aviso: No se realizó ninguna eliminación para: {identificador}")
            
        return None
