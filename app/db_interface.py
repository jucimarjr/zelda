from flask_mysqldb import MySQL
from .tables.funcionario.funcionario_interface import FuncionarioInterface
from .tables.usuario.usuario_interface import UsuarioInterface
from .tables.setor.setor_interface import SetorInterface
from .tables.usuario.usuario_modelo import Usuario
from .tables.perfil.perfil_interface import PerfilInterface
from .tables.funcionalidade.funcionalidade_modelo import Funcionalidade 
from .tables.funcionalidade.funcionalidade_interface import FuncionalidadeInterface

class Zelda(FuncionarioInterface, UsuarioInterface, SetorInterface, PerfilInterface, FuncionalidadeInterface):

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

    def verifica_email(self,email):
        data = self.execute_query("select count(*) as cont_usuarios from usuario where usuario_email ='{}'".format(email))
        return int(data[0]['cont_usuarios']) >0

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

    def get_usuario_pelo_login(self, login):
        data = self.execute_query("select * from usuario where usuario_login = '{}'".format(login))
        if len(data) < 1:
            return None
        usuarios = []
        for d in data:
            usuario = Usuario(
                id=d["usuario_id"],
                login=d["usuario_login"],
                senha=d["usuario_senha"],
                logado=d["usuario_logado"],
                #email=d["usuario_email"],
                #confirmaemail=d["usuario_confirmaemail"],
                perfil_id=d["perfil_id"])
            usuarios.append(usuario)
        return usuarios[0]
    
    def get_funcionalidades_usuario(self,user_id):
        data = self.execute_query("select F.* from funcionalidade as F, permissao as P, usuario as U where P.perfil_id = U.perfil_id AND P.funcionalidade_id = F.funcionalidade_id AND U.usuario_id = '{}'".format(user_id))
        if len(data) < 1:
            return None
        funcionalidades = []
        for d in data:
            funcionalidade = Funcionalidade(
                              funcionalidade_id=d["funcionalidade_id"],
                              funcionalidade_codigo=d["funcionalidade_codigo"],
                              funcionalidade_nome=d["funcionalidade_nome"],
                              funcionalidade_desc=d["funcionalidade_desc"],
                              funcionalidade_caminho=d["funcionalidade_caminho"],
                              funcionalidade_caminho_imagem=d["funcionalidade_caminho_imagem"],
                              funcionalidade_status=d["funcionalidade_status"],
                              sistema_id=d["sistema_id"])
            funcionalidades.append(funcionalidade)
        return funcionalidades
