class Permissao:
    def __init__(self,id=0,funcionalidade_codigo=0,perfil_id=0):
        self.id = id
        self.funcionalidade_codigo = funcionalidade_codigo
        self.perfil_id = perfil_id

    def serializa(self):
        return {
                "id": self.id,
                "funcionalidade_codigo": self.funcionalidade_codigo,
                "perfil_id": self.perfil_id
                }
