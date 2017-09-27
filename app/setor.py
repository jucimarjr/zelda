class Setor:
    def __init__(self,
                 id=0,
                 nome="none",
                 situacao=0,
                 setor_pai="none"):
        self.id = id
        self.nome = nome
        self.situacao = situacao
        self.setor_pai = "none"

    def __str__(self):
        string = "{"
        string += "setor_id:" + str(self.id) + ","
        string += "setor_nome:" + self.nome + ","
        string += "setor_situacao:" + str(self.situacao) + ","
        string += "setor_setor_pai:" + str(setor_pai)
        string += "}"
        return string

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    setor = Setor()
    print(setor)
