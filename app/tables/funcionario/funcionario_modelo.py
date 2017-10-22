from ...cursor import db
from ..lotacao.lotacao_modelo import Lotacao

class Funcionario:

    __funcionario_id = None
    __situacao = 0
    __lotacao = None

    def __init__(self, funcionario_id = None):
        self.nome = None
        #self.caminho_foto = None

        if funcionario_id is not None:

            data = db.get_funcionario(funcionario_id)
            if data is not None:

                self.__funcionario_id = funcionario_id
                self.__situacao = data['funcionario_situacao']
                self.nome = data['funcionario_nome']

                # Pega a última lotação do funcionário (1 argumento)
                lotacao = Lotacao(funcionario_id = funcionario_id)

                if lotacao.get_id() is not None:
                    self.__lotacao = lotacao


    def get_id(self):
        return self.__funcionario_id

    def get_situacao(self):
        return self.__situacao

    def get_setor(self):
        if self.__lotacao is None:
            return None
        
        return self.__lotacao.get_setor()
    
    def mudar_setor(self, setor_id):
        if self.__lotacao is not None:
            if setor_id == self.get_setor().get_id():
                return

        # Cadastra uma nova lotação
        lotacao = Lotacao(setor_id = setor_id, funcionario_id = self.get_id())
        self.__lotacao = lotacao

    def desativa(self):
        if self.__situacao != -1:
            self.__situacao = 1
            db.deleta_funcionario(self.get_id())

    def salva(self):
        if self.get_id() is not None:
            db.edita_funcionario(self)
        else:
            self.__funcionario_id = db.cadastra_funcionario(self)

    def serializa(self):
        return {
                "id": self.get_id(),
                "nome": self.nome,
                "situacao": self.__situacao
                }