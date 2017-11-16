from app.cursor import db
from app.tables.usuario.usuario_modelo import Usuario
from app import app
from app.utils.files import upload

class Processo:

    def __init__(self, processo_id = None):

        self.__processo_id = None
        self.tipo = None
        self.desc = None
        self._usuario = None

        if processo_id is not None:
            data = db.get_processos2(processo_id)
            if data is not None:

                self.__processo_id = processo_id
                self.tipo = data['processo_tipo']
                self.desc = data['processo_desc']

                self.set_usuario(data['usuario_id'])

    def get_id(self):
        return self.__processo_id

    def get_tipo(self):
        return self.tipo

    def get_usuario(self):
        return self.__usuario

    def get_desc(self):
        return self.desc

    def set_usuario(self, usuario_id):
        usuario = Usuario(usuario_id)
        if usuario.get_id() is not None:
            self.__usuario = usuario
            
    def salva(self):
        if self.__processo_id is not None:
            db.edita_processo(self)            
        else:
            self.__processo_id = db.cadastra_processo(self)

    def deleta(self):
        if self.get_id() is not None:
            db.deleta_processos4(self.get_id())
