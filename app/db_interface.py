from flask_mysqldb import MySQL
from .lotacao.models.lotacao import Lotacao
from .setor.models.setor import Setor
from .setor.controllers.setor_interface import Zelda_Setor
from .funcionario.controllers.funcionario_interface import Zelda_Funcionario
from .funcionario.models.funcionario import Funcionario
from .usuario.models.usuario import Usuario
from .usuario.controllers.usuario_interface import  Zelda_Usuario

class Zelda(Zelda_Setor, Zelda_Funcionario, Zelda_Usuario):

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

    def verifica_login(self, login, senha):
        data = self.execute_query("select count(*) from usuario where usuario_login = '{}' and usuario_senha = '{}'".format(login, senha))
        return int(data[0]['count(*)']) > 0

    # função que verifica se o usuário está logado. Utilizado no login único.
    def verifica_logado(self, login):
        data = self.execute_query("select usuario_logado from  usuario where usuario_login = '{}'".format(login))
        if (data[0]['usuario_logado'] == 1):
            return False
        return True

    def set_logado_true(self, login):
        data = self.execute_query("select usuario_id from usuario where usuario_login = '{}'".format(login))
        self.execute_query("update usuario set usuario_logado = 0 where  usuario_id = '{}'".format(data[0]['usuario_id']), True)

    def set_logado_false(self, login):
        data = self.execute_query("select usuario_id from usuario where usuario_login = '{}'".format(login))
        self.execute_query("update usuario set usuario_logado = 1 where usuario_id = '{}'".format(data[0]['usuario_id']), True)

    def verifica_admin(self, login):
        data = self.execute_query("select usuario_admin from usuario where usuario_login = '{}'".format(login))
        if (data[0]['usuario_admin'] == 1):
            return False
        return True

    def set_admin_true(self, login):
        data = self.execute_query("select usuario_id from usuario where usuario_login = '{}'".format(login))
        self.execute_query("update usuario set usuario_admin = 0 where usuario_id = '{}'".format(data[0]['usuario_id']), True)

    def get_usuario_senha(self, login):
        data = self.execute_query("select usuario_senha from usuario where usuario_login = '{}'".format(login))
        return data