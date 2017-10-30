from ...cursor import db
from ..sistema.sistema_modelo import Sistema

class Funcionalidade:

    def __init__(self, funcionalidade_id = None):

        self.__funcionalidade_id = None
        self.__codigo = None
        self.__status = 0
        self.__sistema = None
        self.caminho_imagem = None
        self.nome = None
        self.desc = None
        self.caminho = None

        if funcionalidade_id is not None:
            data = db.get_funcionalidade(funcionalidade_id)
            if data is not None:

                self.__funcionalidade_id = funcionalidade_id
                self.__codigo = data['funcionalidade_codigo']
                self.nome = data['funcionalidade_nome']
                self.desc = data['funcionalidade_desc']
                self.__caminho = data['funcionalidade_caminho']
                self.__caminho_imagem = data['funcionalidade_caminho_imagem']
                self.__status = data['funcionalidade_status']

                self.muda_sistema(data['sistema_id'])

    def get_id(self):
        return self.__funcionalidade_id
    
    def get_codigo(self):
        return self.__codigo
    
    def get_status(self):
        return self.__status

    def desativa(self):
        if self.__status == 0:
            __status = 1
            db.desativa_funcionalidade(self.get_id())
    
    def get_sistema(self):
        return self.__sistema

    def muda_sistema(self, sistema_id):
        sistema = Sistema(sistema_id)
        if sistema.get_id() is not None:

            self.__sistema = sistema
            self.__codigo = sistema.prefixo + str(self.get_id()) #melhorar

    def salva(self):
        if self.get_id() is not None:
            db.edita_funcionalidade(self)
        else:
            self.__funcionalidade_id = db.cadastra_funcionalidade(self)