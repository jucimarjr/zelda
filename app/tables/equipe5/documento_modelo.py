from ...cursor import db
from .processo_modelo import Processo
from app import app

class Documento:

    def __init__(self, documento_id = None):

        self.__documento_id = None
        self.__processo = None
        self.desc = None

        if documento_id is not None:
            data = db.get_documento(documento_id)
            if data is not None:

                self.__documento_id = documento_id
                self.desc = data['documento_desc']
                self.__status = data['documento_status']

                self.set_processo(data['processo_id'])

    def get_id(self):
        return self.__funcionalidade_id
    
    def get_status(self):
        return self.__status
    
    def get_status_texto(self):
        if self.__status == 0:
            return 'Ativado'
        elif self.__status == 1:
            return 'Desativado'
        
        return 'Indefinido'

    def desativa(self):
        if self.__status == 0:
            __status = 1
            db.desativa_documento(self.get_id())
    
    def get_processo(self):
        return self.__processo

    def set_processo(self, processo_id):
        processo = Processo(processo_id)
        if processo.get_id() is not None:
            self.__processo = processo
            #self.__codigo = sistema.prefixo + str(self.get_id()) #melhorar

    def salva(self):
        if self.get_id() is not None:
            db.edita_documento(self)
        else:
            self.__documento_id = db.cadastra_documento(self)
