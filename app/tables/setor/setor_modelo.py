from ...cursor import db

class Setor:

    def __init__(self, setor_id = None):
        self.__setor_id = None
        self.__pai = None
        self.__situacao = 0
        self.nome = ''
        self.__pai = None

        if setor_id is not None:
            data = db.get_setor(setor_id)

            if data is not None:

                self.__setor_id = setor_id
                self.__situacao = data['setor_situacao']
                self.nome = data['setor_nome']
                self.__pai = data['setor_pai']

    def get_id(self):
        return self.__setor_id

    def get_pai(self):
        return self.__pai

    def get_situacao(self):
        return self.__situacao

    def get_situacao_texto(self):
        if self.__situacao == 0:
            return 'Ativado'
        elif self.__situacao == 1:
            return 'Desativado'
        
        return 'Indefinido'

    def set_pai(self, pai):
        if pai is Setor and pai.get_id() is not None:
            self.__pai = pai.get_id()

    def desativa(self):
        if self.__situacao != -1:
            self.__situacao = 1
            db.desativa_setor(self.__setor_id)

    def salva(self):
        if self.__setor_id is not None:
            db.edita_setor(self)
        else:
            self.__id = db.cadastra_setor(self)

    def serializa(self):
        return {
            "id": self.__setor_id,
            "nome": self.nome,
            "situacao": self.__situacao,
            "setor_pai": self.__pai
            }