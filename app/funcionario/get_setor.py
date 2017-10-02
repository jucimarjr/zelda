def get_setor(self, id):
    from app.setor import Setor
    data = self.execute_query("select * from setor where setor_id = {}".format(id))
    if len(data) < 1:
        return None
    setores = []
    for d in data:
        setor = Setor(
            id=d["setor_id"],
            nome=d["setor_nome"],
            situacao=d["setor_situacao"])
        setores.append(setor)
    return setores[0]
