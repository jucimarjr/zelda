from ..cursor import db
from ..features.Equipe_4.tables.processo.processo_modelo import Processo

class ZeldaModelo: 

    @staticmethod
    def lista_processos():
        result = []
        for data in db.get_processos_ids():
            processo = processo(data['processo_id'])
            result.append(processo)

        return result


   
