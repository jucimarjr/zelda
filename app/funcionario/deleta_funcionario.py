def deleta_funcionario(self, funcionario_id):
    self.execute_query(
        "update funcionario set funcionario_situacao = 1 where funcionario_id = '{}'".format(funcionario_id), True)
