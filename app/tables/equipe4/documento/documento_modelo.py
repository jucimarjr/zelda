class Documento:
    lista_tipos = [ "Identidade", "Requerimento", "Declaração"]

    def __init__(self, documento_id = None, processo_id = None):
        self.__id = None
        self.tipo = None
        self.descricao = None
        self.link = None
        self.__processo_id = None

        if documento_id is not None:
            data = db.get_documento(id_documento)
            if len(data) > 0:

                self.__id = data[0]['documento_id']
                self.tipo = data[0]['tipo']
                self.descricao = data[0]['descricao']
                self.link = data[0]['link']
                self.__processo_id = data[0]['processo_id']

        elif processo_id is not None:
            self.__processo_id = processo_id

    def get_id(self):
        return self.__id

    def get_tipo_texto(self):
        if self.tipo in range(0, len(Documento.lista_tipos)):
            return Documento.lista_tipos[self.tipo]

        return 'Indefinido'

    def salva(self):
        if self.__processo_id is not None:
            if self.get_id() is None:
                self.__id = db.cadastra_documento(self, self.__processo_id)
            else:
                db.edita_documento(self)

    def remove(self):
        db.deleta_documento(self.get_id())
        self.__id = None
