from ..cursor import db
from ..tables.setor.setor_modelo import Setor

class ZeldaModelo:

    setores = []

    @staticmethod
    def lista_setores():
        for setor_id in db.get_setores_ids():
            setor = Setor(setor_id)
            ZeldaModelo.setores.append(setor)

        return ZeldaModelo.setores
    
    @staticmethod
    def lista_setores_ativos():
        result = []
        for setor_id in db.get_setores_ativos_ids():
            setor = Setor(setor_id)
            result.append(setor)

        return result

        