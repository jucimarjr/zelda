from ...cursor import db
from ..permissao.permissao_modelo import Permissao
from ..funcionalidade.funcionalidade_modelo import Funcionalidade

class Perfil:

    def __init__(self, perfil_id = None):
        
        self.__perfil_id = None
        self.nome = None
        self.__permissoes = []
        
        if perfil_id is not None:
            data = db.get_perfil(perfil_id)

            if data is not None:
                self.__perfil_id = perfil_id
                self.nome = data[0]['perfil_nome']

                data = db.get_permissoes_ids(perfil_id)
                if data is not None:

                    for linha in data:
                        permissao = Permissao(permissao_id = linha['permissao_id'])
                        self.__permissoes.append(permissao)

    def get_id(self):
        return self.__perfil_id

    def get_funcionalidades(self):
        funcionalidades = []
        
        for p in self.__permissoes:
            funcionalidades.append(p.get_funcionalidade())

        return funcionalidades

    def adiciona_permissao(self, funcionalidade_id = None):
        if self.get_id() is not None:
            if funcionalidade_id is not None:
                permissao = Permissao(self.get_id(), funcionalidade_id)
                if permissao.get_funcionalidade().get_id() is not None:
                    permissao.cadastra()
                    self.__permissoes.append(permissao.serializa())

    def remove_permissao(self, funcionalidade_id = None):
        if self.get_id() is not None:
            if funcionalidade_id is not None:
                permissao = Permissao(self.get_id(), funcionalidade_id)
                if permissao.get_funcionalidade().get_id() is not None:
                    permissao.remove()
                    self.__permissoes.remove(permissao.serializa())

    def salva(self):
        if self.get_id() is None:
            self.__perfil_id = db.cadastra_perfil(self)
        else:
            db.edita_perfil(self)