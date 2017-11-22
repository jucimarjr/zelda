from Estado import Estado
class Remessa:

    estado = None

    def __init__(self, estado):
        self.estado = Estado(estado)
    def get_estado(self):
        return self.estado