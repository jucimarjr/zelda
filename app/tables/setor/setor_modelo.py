class Setor:
    def __init__(self,
                 id=0,
                 nome=None,
                 situacao=0,
                 setor_pai=None):
        self.id = id
        self.nome = nome
        self.situacao = situacao
        self.setor_pai = setor_pai

    def serializa(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "situacao": self.situacao,
            "setor_pai": self.setor_pai
            }
