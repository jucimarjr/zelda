from ....cursor import db
from ...usuario.usuario_modelo import Usuario
from app import app

class Processo:
    
    def __init__(self, processo_id=None):

        self.__processo_id = None
        self.__usuario = None
        self.processo_tipo = None
        self.processo_desc = None

        if processo_id is not None:
            data = db.get_processo(processo_id)
            if len(data) > 0:
                self.__processo_id = processo_id
                self.__usuario = Usuario(usuario_id = data[0]['usuario_id'])
                self.processo_tipo = data[0]['tipo']
                self.processo_desc = data[0]['descricao']

    def get_id(self):
        return self.__processo_id

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        if usuario.get_id() is not None:
            self.__usuario = usuario

    def get_processo_tipo(self):
        return self.processo_tipo

    def get_processo_desc(self):
        return self.processo_desc

    def deleta(self):
        if self.get_id() is not None:
            db.deleta_processo(self.get_id())

    def salva(self):
        if self.get_id() is None:
            self.__processo_id = db.cadastra_processo(self)
        else:
            db.edita_processo(self)
