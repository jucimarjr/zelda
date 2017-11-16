from ....cursor import db
from ..processo.processo_modelo import Processo
from app import app

class Documento:
    
    def __init__(self, documento_id=None):

        self.__documento_id = None
        self.__processo = None
        self.documento_desc = None
        self.documento_tipo = None
        self.documento_caminho = None

        if documento_id is not None:
            data = db.get_documento(documento_id)
            if len(data) > 0:
                self.__documento_id = documento_id
                self.__processo = Processo(processo_id = data[0]['processo_id'])
                self.documento_desc = data[0]['descricao']
                self.documento_tipo = data[0]['tipo']
                self.documento_caminho = data[0]['caminho']

    def get_id(self):
        return self.__documento_id

    def get_processo(self):
        return self.__processo

    def set_processo(self, processo):
        if processo.get_id() is not None:
            self.__processo = processo

    def get_documento_tipo(self):
        return self.documento_tipo

    def get_documento_desc(self):
        return self.documento_desc
    
    def get_documento_caminho(self):
        return self.documento_caminho

    def deleta(self):
        if self.get_id() is not None:
            db.deleta_documento(self.get_id())

    def salva(self):
        if self.get_id() is None:
            self.__documento_id = db.cadastra_documento(self)
        else:
            db.edita_documento(self)
