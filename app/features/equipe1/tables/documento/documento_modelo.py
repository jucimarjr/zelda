from .documento_interface import DocumentoInterface

class Documento:
    def __init__(self, id_documento = None, id_processo = None):
        self.__id = None
        self.tipo = None
        self.descricao = None
        self.__caminho = None
        self.__processo_id = None

        if id_processo is not None:
            if id_documento is not None:
                data = DocumentoInterface.get_documento(id_documento)
                if len(data) > 0:

                    self.__id = data['documento_id']
                    self.tipo = data['tipo']
                    self.descricao = data['descricao']
                    self.__caminho = data['caminho']
                    self.__processo_id = data['processo_id']

    def get_id(self):
        return self.__id

    def get_tipo_texto(self):
        lista_nomes = [ "Identidade", "Requerimento", "Declaração"]

        if self.tipo in range(0, len(lista_nomes)):
            return lista_nomes[self.tipo]

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