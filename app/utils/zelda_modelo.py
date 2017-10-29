from ..cursor import db
from ..tables.setor.setor_modelo import Setor
from ..tables.funcionario.funcionario_modelo import Funcionario

class ZeldaModelo:

    setores = []
    funcionarios = []

    @staticmethod
    def lista_setores():
        ZeldaModelo.setores.clear()
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

    @staticmethod
    def lista_funcionarios():
        result = []
        for data in db.get_funcionarios_ids():
            funcionario = Funcionario(data['funcionario_id'])
            result.append(funcionario)

        return result