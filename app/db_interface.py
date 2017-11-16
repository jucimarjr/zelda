from flask_mysqldb import MySQL
from .tables.funcionario.funcionario_interface import FuncionarioInterface
from .tables.usuario.usuario_interface import UsuarioInterface
from .tables.setor.setor_interface import SetorInterface
from .tables.perfil.perfil_interface import PerfilInterface
from .tables.funcionalidade.funcionalidade_interface import FuncionalidadeInterface
from .tables.sistema.sistema_interface import SistemaInterface
from .tables.equipe_2.processo.processo_interface import ProcessoInterfaceDois
from .tables.equipe_12.processos.processos_interface import ProcessosInterfaceDoze
from .tables.processo_equipe_3.processo_interface import ProcessoInterface
from .features.Equipe_13.tables.processo.processo_interface import ProcessoInterface13
from .tables.equipe4.tables.processo.processo_interface import ProcessoInterfaceQuatro
from .tables.equipe7.processo.processo_interface import ProcessoInterface7
from .tables.equipe7.documento.documento_interface import DocumentoInterface7

class Zelda(FuncionarioInterface, UsuarioInterface, SetorInterface, PerfilInterface, ProcessoInterfaceDois, FuncionalidadeInterface, SistemaInterface, ProcessosInterfaceDoze, ProcessoInterface,ProcessoInterface13,ProcessoInterfaceQuatro,ProcessoInterface7,DocumentoInterface7):


    def __init__(self, app):
        self.mysql = MySQL(app)

    def execute_query(self, query, insert=False):
        cur = self.mysql.connection.cursor()
        cur.execute(query)
        if insert:
            self.mysql.connection.commit()
        else:
            data = cur.fetchall()
            cur.close()
            return data

    def verifica_existe_email(self,email):
        data = self.execute_query("select usuario_id from usuario where usuario_email ='{}'".format(email))
        return data

    def verifica_existe_login(self, login):
        data = self.execute_query("select usuario_id from usuario where usuario_login = '{}'".format(login))
        return data
