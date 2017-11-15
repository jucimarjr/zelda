from ..cursor import db
from app.tables.equipe4.tables.processo.processo_modelo import Processo

class ZeldaModelo: 

    @staticmethod
    def lista_processos():
        result = []
        for data in db.get_processos_ids():
            processo = Processo(data['processo_id'])
            result.append(processo)

        return result


   
