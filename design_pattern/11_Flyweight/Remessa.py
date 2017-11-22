from Estado import Estado
class Remessa:

    __estado = None

    def __init__(self, estado):
        self.__estado = Estado(estado)
    def get_estado(self):
        return self.__estado
