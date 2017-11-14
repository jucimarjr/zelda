from ..cursor import db
from ..features.Equipe_13.tables.processo.processo_modelo import Processo

class ProcessoModelo:

    @staticmethod
    def listar_processos():
        result = []
        for data in db.get_processos_ids():
            processo = Processo(data['processo_id'])
            result.append(processo)

        return result
