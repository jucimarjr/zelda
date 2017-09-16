class Setor:
    def __init__(self,
                 id=0,
                 nome="none",
                 situacao=0):
        self.id = id
        self.nome = nome
        self.situacao = situacao

    def __str__(self):
        string = "{"
        string += "id:" + str(self.id) + ","
        string += "nome:" + self.nome + ","
        string += "situacao:" + str(self.situacao)
        string += "}"
        return string

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    setor = Setor()
    print(setor)
