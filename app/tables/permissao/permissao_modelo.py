class Permissao:
    def __init__(self,id=0,funcionalidade_id=0,perfil_id=0):
        self.id = id
        self.funcionalidade_id = funcionalidade_id
        self.perfil_id = perfil_id

    def serializa(self):
        return {
                "id": self.id,
                "funcionalidade_id": self.funcionalidade_id,
                "perfil_id": self.perfil_id
                }
