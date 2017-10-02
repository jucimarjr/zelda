class Lotacao:
    def __init__(self, id=0, funcionario_id=0, setor_id=0):
        self.id = id
        self.funcionario_id = funcionario_id
        self.setor_id = setor_id

    def __str__(self):
        string = "{"
        string += "id:" + str(self.id) + ","
        string += "funcionario_id:" + self.funcionario_id + ","
        string += "setor_id:" + self.setor_id + ","
        string += "}"
        return string

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    lotacao = Lotacao()
    print(lotacao)
