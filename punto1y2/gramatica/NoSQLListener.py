# Generated from NoSQL.g4 by ANTLR 4.13.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NoSQLParser import NoSQLParser
else:
    from NoSQLParser import NoSQLParser

class NoSQLVisitor(ParseTreeVisitor):

    # inicio del programa
    def visitInicio(self, ctx:NoSQLParser.InicioContext):
        return self.visitChildren(ctx)

    # operaciones individuales
    def visitOperacion(self, ctx:NoSQLParser.OperacionContext):
        return self.visitChildren(ctx)

    # logicaagregar
    def visitCmd_insertar(self, ctx:NoSQLParser.Cmd_insertarContext):
        print(f"Ejecutando inserción en la colección...")
        return self.visitChildren(ctx)

    # logicaobtener
    def visitCmd_buscar(self, ctx:NoSQLParser.Cmd_buscarContext):
        print(f"Buscando datos...")
        return self.visitChildren(ctx)

    # logicacambiar
    def visitCmd_modificar(self, ctx:NoSQLParser.Cmd_modificarContext):
        print(f"Modificando registros...")
        return self.visitChildren(ctx)

    # logicaquitar
    def visitCmd_remover(self, ctx:NoSQLParser.Cmd_removerContext):
        print(f"Eliminando datos de la entidad...")
        return self.visitChildren(ctx)
        
    def visitId_entidad(self, ctx:NoSQLParser.Id_entidadContext):
        return ctx.getText()

    def visitDato(self, ctx:NoSQLParser.DatoContext):
        return ctx.getText()
