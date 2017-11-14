from ..cursor import db
from ..tables.processos.processos_modelo import Processo

class ProcessaModelo:

    @staticmethod
    def listar_processos():
        result = []
        for data in db.get_processos_ids():
            processo = Processo(data['processo_id'])
            result.append(processo)

        return result
