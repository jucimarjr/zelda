def cadastra_lotacao(self, lotacao):
    self.execute_query(
        "insert into lotacao (funcionario_id, setor_id)  values('{}', '{}')".format(lotacao.funcionario_id,
                                                                                    lotacao.setor_id), True)
