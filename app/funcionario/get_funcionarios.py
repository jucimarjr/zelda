def get_funcionarios(self):
    from app.funcionario import Funcionario
    data = self.execute_query('''select funcionario_id, funcionario_nome, funcionario_situacao from funcionario''')
    funcionarios = []
    for d in data:
        funcionario = Funcionario(
            id=d["funcionario_id"],
            nome=d["funcionario_nome"],
            situacao=d["funcionario_situacao"])
        funcionarios.append(funcionario)
    return funcionarios
