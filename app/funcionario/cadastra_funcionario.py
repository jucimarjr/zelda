def cadastra_funcionario(self, funcionario):
    self.execute_query("insert into funcionario (funcionario_nome) values ('{}')".format(funcionario.nome), True)
