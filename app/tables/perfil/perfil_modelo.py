class Perfil:

    __perfil_id = None

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
    def get_id(self):
        return self.__perfil_id