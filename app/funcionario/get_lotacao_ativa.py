def get_lotacao_ativa(self, funcionario_id):
    from zelda.app.lotacao import Lotacao
    data = self.execute_query(
        "select * from lotacao where lotacao.funcionario_id = '{}' order by lotacao.lotacao_id desc limit 1".format(
            funcionario_id))

    if len(data) < 1:
        return None

    for d in data:
        lotacao = Lotacao(
            id=d["lotacao_id"],
            funcionario_id=d["funcionario_id"],
            setor_id=d["setor_id"])

    return lotacao
