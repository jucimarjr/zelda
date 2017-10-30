from ...cursor import db
from ..funcionalidade.funcionalidade_modelo import Funcionalidade

class Permissao:

    def __init__(self, permissao_id = None, funcionalidade = None, perfil = None):
        self.__permissao_id = None
        self.__funcionalidade = None
        self.__perfil_id = None

        if permissao_id is not None:
            data = db.get_permissao(permissao_id)

            if data is not None:
                if len(data) > 0:
                    self.__permissao_id = permissao_id
                    self.__funcionalidade = Funcionalidade(data[0]['funcionalidade_id'])

                    return
        
        if funcionalidade is not None and perfil is not None:
            if funcionalidade.get_id() is not None and perfil.get_id() is not None:
                self.__funcionalidade = funcionalidade
                self.__perfil_id = perfil.get_id()


    def get_id(self):
        return self.__permissao_id

    def get_funcionalidade(self):
        return self.__funcionalidade

    def get_perfil_id(self):
        return self.__perfil_id

    def cadastra(self):
        if self.__perfil_id is not None and self.get_id() is None:
            self.__permissao_id = db.cadastra_permissao(self)

    def remove(self):
        if self.get_id() is not None:
            db.remove_permissao(self.get_id())