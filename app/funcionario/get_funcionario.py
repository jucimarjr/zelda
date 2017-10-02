def get_funcionario(self, id):
    from app.funcionario import Funcionario
    data = self.execute_query(
        '''select funcionario_id, funcionario_nome, funcionario_situacao from funcionario where  funcionario_id = {}'''.format(
            id))
    if len(data) < 1:
        return None
    funcionarios = []
    for d in data:
        funcionario = Funcionario(
            id=d["funcionario_id"],
            nome=d["funcionario_nome"],
            situacao=d["funcionario_situacao"])
        funcionarios.append(funcionario)
    return funcionarios[0]
