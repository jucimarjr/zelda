class Perfil:
    def __init__(self,
                 id=0,
                 nome="none"):
        self.id = id
        self.nome = nome

    def serializa(self):
        return {
                "id": self.id,
                "nome": self.nome,
                }
