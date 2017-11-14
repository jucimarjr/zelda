from ...cursor import db

class Processo:

    def __init__(self, processo_id = None):
        self.__processo_id = None
        self.desc = ''
        self.tipo = ''
        self.__situacao = 0

        if processo_id is not None:
            data = db.get_processo(processo_id)

            if data is not None:

                self.__processo_id = processo_id
                self.desc = data['processo_desc']
                self.tipo = data['processo_tipo']
                self.__situacao = data['processo_situacao']
                

    def get_id(self):
        return self.__processo_id

    def get_situacao(self):
        return self.__situacao

    def get_situacao_texto(self):
        if self.__situacao == 0:
            return 'Ativado'
        elif self.__situacao == 1:
            return 'Desativado'
        
        return 'Indefinido'


    def desativa(self):
        if self.__situacao != -1:
            self.__situacao = 1
            db.desativa_processo(self.__processo_id)

    def salva(self):
        if self.__processo_id is not None:
            db.edita_processo(self)
        else:
            self.__id = db.cadastra_processo(self)

    def serializa(self):
        return {
            "id": self.__setor_id,
            "desc": self.nome,
            "tipo": self.tipo,
            "situacao": self.__situacao
            }
