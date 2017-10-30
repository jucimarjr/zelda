from ...cursor import db
from ...tables.setor.setor_modelo import Setor

class Lotacao:

    def __init__(self, funcionario_id, setor_id = None):
        self.__id = None
        self.__setor = None
        self.__id = None

        if setor_id is None:
            data = db.get_lotacao_ativa(funcionario_id)

            if data is not None:

                self.__id = data['lotacao_id']
                self.__setor = Setor(data['setor_id'])

            else:
                setor = Setor(setor_id)
                if setor.get_id() is not None:
                    self.__setor = setor
                    self.__id = db.cadastra_lotacao(funcionario_id, self)

        else:
            setor = Setor(setor_id)
            if setor.get_id() is not None:
                self.__setor = setor
                self.__id = db.cadastra_lotacao(funcionario_id, self)

    def get_setor(self):
        return self.__setor

    def get_id(self):
        return self.__id