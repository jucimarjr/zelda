from ....cursor import db

class Processo12:

    def __init__(self,processo_id = None):

        self.__processo_id = None
        self.__usuario_id = None
        self.tipo = None
        self.desc = None
        self.status = 0

        if processo_id is not None:

            data = db.get_processo_12(processo_id)
            if data is not None:

                self.__processo_id = processo_id
                self.tipo = data['processo_tipo']
                self.desc = data['processo_desc']
                self.__usuario_id = data['usuario_id']
                self.__status = data['processo_status']


    def get_id_12(self):
        return self.__processo_id

    def get_status_12(self):
        return self.__status

    def get_situacao_texto_12(self):
        if self.__status ==0:
            return 'Ativado'
        elif self.__status ==1:
            return 'Desativado'

        return 'Indefinido'

    def salva(self):
        if self.__processo_id is not None:
            db.edita_processo_12(self)
        else:
            self.__processo_id = db.cadastra_processo(self)

    def desativa(self):
        if self.__status != -1:
            self.__status= 1
            db.desativa_processo_12(self.__processo_id)
