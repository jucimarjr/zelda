from ..cursor import db
from app.tables.equipe4.tables.processo.processo_modelo import Processo
from ..tables.usuario.usuario_modelo import Usuario

class ZeldaModelo: 

    @staticmethod
    def lista_processos():
        result = []
        for data in db.get_processos_ids():
            processo = Processo(data['processo_id'])
            result.append(processo)

        return result

    @staticmethod
    def lista_usuarios():
        result = []
        for data in db.get_usuarios_ids():
            usuario = Usuario(data['usuario_id'])
            result.append(usuario)

        return result


   
