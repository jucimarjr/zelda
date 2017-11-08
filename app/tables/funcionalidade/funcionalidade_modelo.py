from ...cursor import db
from ..sistema.sistema_modelo import Sistema
from app import app
from ...utils.files import upload

class Funcionalidade:

    def __init__(self, funcionalidade_id = None):

        self.__funcionalidade_id = None
        self.__codigo = None
        self.__status = 0
        self.__sistema = None
        self.__caminho_imagem = None
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
                self.caminho = data['funcionalidade_caminho']
                self.__caminho_imagem = data['funcionalidade_caminho_imagem']
                self.__status = data['funcionalidade_status']

                self.set_sistema(data['sistema_id'])

    def get_id(self):
        return self.__funcionalidade_id
    
    def get_codigo(self):
        return self.__codigo

    def get_status(self):
        return self.__status

    def get_caminho_imagem(self):
        return self.__caminho_imagem
    
    def get_status_texto(self):
        if self.__status == 0:
            return 'Ativado'
        elif self.__status == 1:
            return 'Desativado'
        
        return 'Indefinido'

    def desativa(self):
        if self.__status == 0:
            __status = 1
            db.desativa_funcionalidade(self.get_id())
    
    def get_sistema(self):
        return self.__sistema

    def set_sistema(self, sistema_id):
        sistema = Sistema(sistema_id)
        if sistema.get_id() is not None:
            self.__sistema = sistema
            self.__codigo = sistema.prefixo + str(self.get_id()) #melhorar

    def set_imagem(self, arquivo_input):
        if self.get_id() is not None:
            caminho = upload(app.config['FUNCIONALIDADES_UPLOAD_PATH'], arquivo_input, self.get_id())
            if caminho is not None:
                self.__caminho_imagem = caminho
                db.edita_funcionalidade_caminho_imagem(self)

    def salva(self):
        if self.get_id() is not None:
            db.edita_funcionalidade(self)
        else:
            self.__funcionalidade_id = db.cadastra_funcionalidade(self)