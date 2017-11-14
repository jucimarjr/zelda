from .documento_interface import DocumentoInterface

class Documento:
    lista_tipos = [ "Identidade", "Requerimento", "Declaração"]

    def __init__(self, id_documento = None, id_processo = None):
        self.__id = None
        self.tipo = None
        self.descricao = None
        self.caminho = None
        self.__processo_id = None

        if id_documento is not None:
            data = DocumentoInterface.get_documento(id_documento)
            if len(data) > 0:

                self.__id = data[0]['documento_id']
                self.tipo = data[0]['tipo']
                self.descricao = data[0]['descricao']
                self.caminho = data[0]['caminho']
                self.__processo_id = data[0]['processo_id']

        elif id_processo is not None:
            self.__processo_id = id_processo

    def get_id(self):
        return self.__id

    def get_tipo_texto(self):
        if self.tipo in range(0, len(Documento.lista_tipos)):
            return Documento.lista_tipos[self.tipo]

        return 'Indefinido'

    def salva(self):
        if self.__processo_id is not None:
            if self.get_id() is None:
                self.__id = DocumentoInterface.cadastra_documento(self, self.__processo_id)
            else:
                DocumentoInterface.edita_documento(self)

    def remove(self):
        DocumentoInterface.deleta_documento(self.get_id())
        self.__id = None