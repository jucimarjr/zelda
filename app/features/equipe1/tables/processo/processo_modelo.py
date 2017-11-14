from .processo_interface import ProcessoInterface
from ..documento.documento_interface import DocumentoInterface
from .....tables.usuario.usuario_modelo import Usuario
from ..documento.documento_modelo import Documento

class Processo:
    lista_tipos = [ "Segunda Chamada", "Solicitação de Matrícula",\
            "Aproveitamento de Matéria", "Trancamento de Matéria", "Segunda via de Carteira do RU"]

    def __init__(self, id_processo = None, usuario = None):
        self.__id = None
        self.tipo = None
        self.descricao = None
        self.__usuario = None
        self.__documentos = []

        if id_processo is not None:
            data = ProcessoInterface.get_processo(id_processo)
            if len(data) > 0:

                self.__id = data[0]['processo_id']
                self.tipo = data[0]['tipo']
                self.descricao = data[0]['descricao']
                usuario = Usuario(data[0]['usuario_id'])

                data = DocumentoInterface.get_documentos_ids_por_processo(self.get_id())
                for i in range(0, len(data)):
                    documento = Documento(data[i]['documento_id'])
                    self.__documentos.append(documento)

                if usuario.get_id() is not None:
                    self.__usuario = usuario
        else:
            self.__usuario = usuario

    def get_id(self):
        return self.__id

    def get_documento(self, documento_id):
        for i in range(0, len(self.get_documentos())):
            if self.get_documentos()[i].get_id() == documento_id:
                return self.get_documentos()[i]

        return None

    def get_usuario(self):
        return self.__usuario

    def get_tipo_texto(self):
        if self.tipo in range(0, len(Processo.lista_tipos)):
            return Processo.lista_tipos[self.tipo]

        return 'Indefinido'

    def salva(self):
        if self.get_usuario() is not None:
            if self.get_usuario().get_id() is not None:
                if self.get_id() is None:
                    self.__id = ProcessoInterface.cadastra_processo(self)
                else:
                    ProcessoInterface.edita_processo(self)

    def remove(self):
        for documento in self.get_documentos():
            if document.get_id() is not None:
                DocumentoInterface.deleta_documento(documento.get_id())
                
        ProcessoInterface.deleta_processo(self.get_id())
        self.__id = None

    def get_documentos(self):
        return self.__documentos

    def adiciona_documento(self, documento):
        if documento.get_id() is not None and documento not in self.get_documentos():
            self.__documentos.append(documento)

    def remove_documento(self, documento_id):
        for i in range(0, len(self.get_documentos())):
            if documento_id == self.get_documentos()[i].get_id():
                self.__documentos.remove(self.get_documentos()[i])
                DocumentoInterface.deleta_documento(documento_id)

    def set_usuario(self, usuario):
        if usuario.get_id() is not None:
            self.__usuario = usuario
            ProcessoInterface.edita_processo_usuario(self)