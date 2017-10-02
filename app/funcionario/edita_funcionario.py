def edita_funcionario(self, funcionario):
    self.execute_query(
        "update funcionario set funcionario_nome = '{}', funcionario_situacao ='{}' where funcionario_id = '{}'".format(
            funcionario.nome, funcionario.situacao, funcionario.id), True)
