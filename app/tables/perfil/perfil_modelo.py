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

    def salva(self):
        if self.get_id() is None:
            self.__perfil_id = db.cadastra_perfil(self)
        else:
            db.edita_perfil(self)

    def deleta(self):
        if self.get_id() is not None:
            db.deleta_perfil(self.get_id())

    def altera_funcionalidades(self, novas_funcionalidades):
        self.__funcs_novas = []
        self.__perms_removidas = []

        for n in novas_funcionalidades:
            if n not in [(f.get_id()) for f in self.get_funcionalidades()]:
                self.__funcs_novas.append(n)

        for p in self.__permissoes:
            if p.get_funcionalidade().get_id() not in novas_funcionalidades:
                self.__perms_removidas.append(p)

        for n in self.__funcs_novas:
            permissao = Permissao(funcionalidade = Funcionalidade(n), perfil = self)
            permissao.cadastra()
            self.__permissoes.append(permissao)
        
        for r in self.__perms_removidas:
            db.remove_permissao(r.get_id())
            self.__permissoes.remove(r)

        self.__funcs_novas = []
        self.__funcs_removidas = []