class Funcionario:
    def __init__(self,
                 id=0,
                 nome="none",
                 situacao="none"):
        self.id = id
        self.nome = nome
        self.situacao = situacao
        

    def __str__(self):
        string = "{"
        string += "funcionario_id:" + str(self.id) + ","
        string += "funcionario_nome:" + self.nome + ","
        string += "funcionario_situacao:" + str(self.situacao) 
        string += "}"

        return string

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    funcionario = Funcionario()
    print(funcionario)
