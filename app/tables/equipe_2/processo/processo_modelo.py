from ....cursor import db

class Processo:

    def __init__(self, processo_id = None):
        self.__id = None
        self.__id_usuario = None
        self.__descricao = None
        self.__tipo = None
        self.__situacao = 0
        '''
        if processo_id is not None:
            data = db.get_processo_id(processo_id)

            if data is not None:

                self.__id = processo_id
                self.__id_usuario = data['id_usuario']
                self.__descricao = data['descricao']
                self.__tipo = data['tipo']
                self.__situacao = data['situacao']
        '''
        data = {}
        data['id'] = 1
        data['id_usuario'] = 2
        data['descricao'] = "teste"
        data['tipo']  = 3
        data['situacao']  = 2

        self.__id = data['id']
        self.__id_usuario = data['id_usuario']
        self.__descricao = data['descricao']
        self.__tipo = data['tipo']
        self.__situacao = data['situacao']

    def get_situacao(self):
        return self.__situacao

    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao

    def get_tipo(self):
        return self.__tipo

    def get_id_usuario(self):
        return self.__id_usuario

    def serializa(self):
        return {
                "id": self.get_id(),
                "id_usuario": self.get_id_usuario(),
                "descricao": self.get_descricao(),
                "tipo": self.get_tipo()
                }

       