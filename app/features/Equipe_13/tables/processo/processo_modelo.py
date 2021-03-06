from .....cursor import db
from .....tables.usuario.usuario_modelo import Usuario
from app import app
from .processo_interface import *

class Processo:
    
    def __init__(self, processo_id=None,usuario = None):

        self.__processo_id = None
        self.__descricao = None
        self.__tipo = None
        self.__usuario = None

        if processo_id is not None:
            data = db.get_processo_13(processo_id)
            if len(data) > 0:
                self.__processo_id = processo_id
                self.__descricao = data['processo_descricao']
                self.__tipo = data['processo_tipo']
                usuario = Usuario(data['usuario_id'])
            if usuario.get_id() is not None:
                    self.__usuario = usuario
        else:
            self.__usuario = usuario

    def get_id(self):
        return self.__processo_id

    def get_descricao(self):
        return self.__descricao

    def get_tipo(self):
        return self.__tipo
    
    def get_usuario(self):
        return self.__usuario

    def set_descricao(self,descricao):
        if descricao.get_id() is not None:
            self.__descricao = descricao
    
    def deleta_13(self):
        db.deleta_processo_13(self.get_id())

    def salva(self):
        if self.get_id() is None:
            self.__processo_id = db.cadastra_processo_13(self)
        else:
            db.edita_processo_13(self)

    def set_usuario(self, usuario):
        if usuario.get_id() is not None:
            self.__usuario = usuario
            ProcessoInterface.edita_processo_usuario_13(self)
