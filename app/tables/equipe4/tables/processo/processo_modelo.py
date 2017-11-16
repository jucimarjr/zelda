from app.cursor import db
from app.tables.usuario.usuario_modelo import Usuario
from app import app
from app.utils.files import upload
from .processo_interface import *

class Processo:

    def __init__(self, processo_id = None, usuario = None):

        self.__processo_id = None
        self.tipo = None
        self.desc = None
        self.__usuario = None

        if processo_id is not None:
            data = db.get_processos_4(processo_id)
            if len(data) > 0:
                self.__processo_id = processo_id
                self.tipo = data['processo_tipo']
                self.desc = data['processo_desc']

                usuario = Usuario(data['usuario_id'])
                if usuario.get_id() is not None:
                    self.__usuario = usuario
            else:
                self.__usuario = usuario

    def get_id(self):
        return self.__processo_id

    def get_tipo(self):
        return self.tipo

    def get_usuario(self):
        return self.__usuario

    def get_desc(self):
        return self.desc

    def salva(self):
        if self.get_id() is None:
            self.__processo_id = db.cadastra_processo4(self)
        else:
            db.edita_processo_4(self)
            

    def deleta(self):
        if self.get_id() is not None:
            db.deleta_processos4(self.get_id())
            
    def set_usuario(self, usuario):
        if usuario.get_id() is not None:
            self.__usuario = usuario
