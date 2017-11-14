from ....cursor import db
from ....utils.files import upload
from ....utils.criptografador import Criptografador
from app import app


class Documento:
    def __init__(self, documento_id=None):

        self.__documento_id = None
        self.id = None
        self.tipo = None
        self.desc = None
        self.__status = 0
        self.__caminho_foto = 'user_profile.jpg'

        if documento_id is not None:
            data = db.get_documento(documento_id)
            if data is not None:
                self.__documento_id = documento_id
                self.id = data['documento_id']
                self.tipo = data['documento_tipo']
                self.desc = data['documento_desc']
                self.__caminho_foto = data[0]['documento_caminho_foto']
                self.__status = data['documento_status']

    def get_id(self):
        return self.__documento_id

    def get_status(self):
        return self.__status

    def get_status_texto(self):
        if self.__status == 0:
            return 'Ativado'
        elif self.__status == 1:
            return 'Desativado'

        return 'Indefinido'
    
    def get_caminho_foto(self):
        return self.__caminho_foto
    
    def desativa(self):
        if self.__status == 0:
            self.__status = 1
            db.desativa_documento(self.get_id())

    def ativa(self):
        if self.__status == 1:
            self.__status = 0
            db.ativa_documento(self.get_id())

    def salva(self):
        if self.__documento_id is not None:
            db.edita_documento(self)
        else:
            self.__documento_id = db.cadastra_documento(self)
    
    def set_foto(self, arquivo_input):
        if self.get_id() is not None:
            caminho = upload(app.config['documentoS_UPLOAD_PATH'], arquivo_input, self.get_id())
            if caminho is not None:
                self.__caminho_foto = caminho
                db.edita_documento_caminho_foto(self)