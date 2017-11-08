from ..cursor import db
from ..tables.setor.setor_modelo import Setor
from ..tables.funcionario.funcionario_modelo import Funcionario
from ..tables.usuario.usuario_modelo import Usuario
from ..tables.perfil.perfil_modelo import Perfil
from ..tables.funcionalidade.funcionalidade_modelo import Funcionalidade
from ..tables.sistema.sistema_modelo import Sistema

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

    @staticmethod
    def lista_usuarios():
        result = []
        for data in db.get_usuarios_ids():
            usuario = Usuario(data['usuario_id'])
            result.append(usuario)

        return result

    @staticmethod
    def lista_perfis():
        result = []
        for data in db.get_perfis_ids():
            perfil = Perfil(data['perfil_id'])
            result.append(perfil)

        return result

    @staticmethod
    def lista_funcionalidades(id = None):
        result = []
        for data in db.get_funcionalidades_ids():
            funcionalidade = Funcionalidade(data['funcionalidade_id'])
            if id is not None:
                if funcionalidade.get_sistema().get_id() == id:
                    result.append(funcionalidade)
            else:
                result.append(funcionalidade)
        return result

    @staticmethod
    def lista_sistemas():
        result = []
        for data in db.get_sistemas_ids():
            sistema = Sistema(data['sistema_id'])
            result.append(sistema)

        return result

    @staticmethod
    def pesquisa_funcionalidade(caminho):
        data = db.get_funcionalidade_id_por_caminho(caminho)
        if len(data) < 1:
            return None

        funcionalidade = Funcionalidade(data[0]['funcionalidade_id'])
        if funcionalidade.get_id() is None:
            return None

        return funcionalidade