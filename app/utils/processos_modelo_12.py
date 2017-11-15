from ..cursor import db
from ..tables.equipe_12.processos.processos_modelo import Processo12

class ProcessaModelo:

    @staticmethod
    def listar_processos():
        result = []
        for data in db.get_processos_ids():
            processo = Processo12(data['processo_id'])
            result.append(processo)

        return result
