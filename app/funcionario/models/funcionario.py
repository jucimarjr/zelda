class Funcionario:
    def __init__(self,
                 id=0,
                 nome=None,
                 situacao=0):
        self.id = id
        self.nome = nome
        self.situacao = situacao

    def serializa(self):
        return {
                "id": self.id,
                "nome": self.nome,
                "situacao": self.situacao
                }