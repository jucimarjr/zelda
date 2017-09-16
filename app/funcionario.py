class Funcionario:
    def __init__(self,
                 id=0,
                 nome="none",
                 situacao="none",
                 setor_id="none",
                 setor_nome="none",
                 setor_situacao=0):
        self.id = id
        self.nome = nome
        self.situacao = situacao
        self.setor_id = setor_id
        self.setor_nome = setor_nome
        self.setor_situacao = setor_situacao
        

    def __str__(self):
        string = "{"
        string += "id:" + str(self.id) + ","
        string += "nome:" + self.nome + ","
        string += "situacao:" + str(self.situacao) + ","
        string += "setor_id:" + str(self.setor_id) + ","
        string += "setor_nome:" + self.setor_nome + ","
        string += "setor_situacao:" + str(self.setor_situacao) + ","
        string += "}"

        return string

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    funcionario = Funcionario()
    print(funcionario)
