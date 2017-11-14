from ....cursor import db


class Processo:
    def __init__(self, processo_id=None):

        self.__processo_id = None
        self.id = None
        self.tipo = None
        self.__status = 0

        if processo_id is not None:
            data = db.get_processo(processo_id)
            if data is not None:
                self.__processo_id = processo_id
                self.id = data['processo_id']
                self.tipo = data['processo_desc']
                self.__status = data['processo_status']

    def get_id(self):
        return self.__processo_id

    def get_status(self):
        return self.__status

    def get_status_texto(self):
        if self.__status == 0:
            return 'Ativado'
        elif self.__status == 1:
            return 'Desativado'

        return 'Indefinido'

    def desativa(self):
        if self.__status == 0:
            self.__status = 1
            db.desativa_processo(self.get_id())

    def ativa(self):
        if self.__status == 1:
            self.__status = 0
            db.ativa_processo(self.get_id())

    def salva(self):
        if self.__processo_id is not None:
            db.edita_processo(self)
        else:
            self.__processo_id = db.cadastra_processo(self)