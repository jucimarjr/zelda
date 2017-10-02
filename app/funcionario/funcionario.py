from app.funcionario import get_funcionarios, get_lotacao_ativa, cadastra_funcionario, cadastra_lotacao, \
    get_setor, get_funcionario, deleta_funcionario, edita_funcionario, serializa


class Funcionario:
    def __init__(self,
                 id=0,
                 nome=None,
                 situacao=0):
        self.id = id
        self.nome = nome
        self.situacao = situacao

    def serializa(self):
        return serializa(self)

    # CRUD - FUNCIONARIO

    def cadastra_funcionario(self, funcionario):
        return cadastra_funcionario(funcionario)

    def cadastra_lotacao(self, lotacao):
        return cadastra_lotacao(self, lotacao)

    def get_lotacao_ativa(self, funcionario_id):
        return get_lotacao_ativa(self, funcionario_id)

    def get_funcionarios(self):
        return get_funcionarios(self)

    def edita_funcionario(self, funcionario):
        return edita_funcionario(self, funcionario)

    def deleta_funcionario(self, funcionario_id):
        return deleta_funcionario(self, funcionario_id)

    def get_funcionario(self, id):
        return get_funcionario(self, id)

    def get_setor(self, id):
        return get_setor(self, id)
