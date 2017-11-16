from ...cursor import db
from  ..usuario.usuario_modelo import Usuario
from app import app

class Processo:
    
    def __init__(self, processo_id=None):

        self.__id = None
        self.descricao = None
        self.tipo = None
        self.__usuario_id = None
        self.situacao = None
        #self.documento = None

        if processo_id is not None:
            data = db.get_processo(processo_id)
            if len(data) > 0:
                self.__id = processo_id
                self.descricao = data[0]['descricao']
                self.tipo = data[0]['tipo']
                self.__usuario_id = data[0]['usuario_id']
                self.situacao = data[0]['situacao']


    def get_id(self):
        return self.__id

    def get_usuario_id(self):
        return self.__usuario_id

    
    def desativa(self):
        db.desativa_processo(self.get_id())

    def salva(self):
        if self.get_id() is None:
            self.__id = db.cadastra_processo(self)
        else:
            db.edita_processo(self)
