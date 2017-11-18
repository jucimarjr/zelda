from ...cursor import db

class Processo:

    def __init__(self, processo_id = None):
        self.__processo_id = None
        self.__usuario_id = None
        self.__descricao = None
        self.__tipo = None
        self.__status = 0

        if processo_id is not None:
            data = db.get_processo(processo_id)

            if data is not None:

                self.__processo_id = processo_id
                self.__usuario_id = data['usuario_id']
                self.__descricao = data['processo_descricao']
                self.__tipo = data['processo_tipo']
                self.__status = data['processo_status']


    def get_id(self):
        return self.__processo_id

    def get_status(self):
        return self.__status

    def get_status_texto(self):
        if self.__situacao == 0:
            return 'Ativado'
        elif self.__situacao == 1:
            return 'Desativado'

        return 'Indefinido'

    def get_descricao(self):
        return self.__descricao

    def get_tipo(self):
        return self.__tipo

    def get_id_usuario(self):
        return self.__usuario_id

    def desativa(self):
        if self.__situacao != -1:
            self.__situacao = 1
            db.desativa_processo(self.__processo_id)

    def serializa(self):
        return {
            "id": self.get_id(),
            "id_usuario": self.get_id_usuario(),
            "descricao": self.get_descricao(),
            "tipo": self.get_tipo()
            }

    def salva(self,d,t,i,u):
        if self.get_id() is not None:
            db.edita_processo(d,t,i,u)
        else:
            self.__id = db.cadastra_processo(d,t,i,u)
