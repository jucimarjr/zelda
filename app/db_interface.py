from flask_mysqldb import MySQL

from .funcionario import Funcionario, cadastra_funcionario, cadastra_lotacao, get_lotacao_ativa, get_funcionarios, \
    edita_funcionario, deleta_funcionario, get_funcionario, get_setor
from .lotacao import Lotacao
from .setor import Setor
from .usuario import cadastra_usuario, get_usuarios, get_usuarios_logados, get_usuarios_admin, edita_usuario, deleta_usuario, serializa, Usuario


class Zelda:

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
        data = self.execute_query("select usuario_admin from funcionario where usuario_login = '{}'".format(login))
        if (data[0]['usuario_admin'] == 1):
            return False
        return True

    def set_admin_true(self, login):
        data = self.execute_query("select usuario_id from usuario where usuario_login = '{}'".format(login))
        self.execute_query("update usuario set usuario_admin = 0 where usuario_id = '{}'".format(data[0]['usuario_id']), True)

    def get_usuario_senha(self, login):
        data = self.execute_query("select usuario_senha from usuario where usuario_login = '{}'".format(login))
        return data

    # CRUD - FUNCIONARIO

    def cadastra_funcionario(self, funcionario):
        return cadastra_funcionario(self, funcionario)

    def cadastra_lotacao(self, lotacao):
        return cadastra_lotacao(self, lotacao)

    def get_lotacao_ativa(self, funcionario_id):
        return get_lotacao_ativa(self, funcionario_id)

    def get_funcionarios(self):
        return get_funcionarios(self)

    def edita_funcionario(self, funcionario):
        return edita_funcionario(self, funcionario)

    def deleta_funcionario(self, funcionario_id):
        return deleta_funcionario(self, funcionario_id)

    def get_funcionario(self, id):
        return get_funcionario(self, id)

    def get_setor(self, id):
        return get_setor(self, id)

    # CRUD - USUARIO

    def serializa(self):
        return serializa(self)

    def cadastra_usuario(self, usuario):
        return cadastra_usuario(self, usuario)

    def get_usuarios(self):
        return get_usuarios(self)

    def get_usuarios_logados(self):
        return get_usuarios_logados(self)

    def get_usuarios_admin(self):
        get_usuarios_admin(self)

    def edita_usuario(self, usuario):
        edita_usuario(self, usuario)

    def deleta_usuario(self, usuario_id):
        deleta_usuario(self, usuario_id)

    # CRUD - SETOR

    def cadastra_setor(self, setor):
        self.execute_query("insert into setor (setor_nome) values (\"{}\")".format(setor.nome), True)

    def get_setores(self):
        data = self.execute_query("select * from setor")
        setores = []
        for d in data:
            setor = Setor(
                id=d["setor_id"],
                nome=d["setor_nome"],
                situacao=d["setor_situacao"])
            setores.append(setor)
        return setores

    def get_setores_ativos(self):
        data = self.execute_query("select * from setor where setor_situacao = 0")
        setores = []
        for d in data:
            setor = Setor(
                id=d["setor_id"],
                nome=d["setor_nome"],
                situacao=d["setor_situacao"])
            setores.append(setor)
        return setores

    def edita_setor(self, setor):
        self.execute_query("update setor set setor_nome = '{}' where setor_id = '{}'".format(setor.nome, setor.id), True)

    def deleta_setor(self, setor_id):
        self.execute_query("update setor set setor_situacao = 1  where setor_id = '{}'".format(setor_id), True)

    
    # CRUD - USUARIO

    def get_usuarios(self):
        data = self.execute_query('''select * from usuario''')
        usuarios = []
        for d in data:
            usuario = Usuario(
                          id=d["usuario_id"],
                          login=d["usuario_login"],
                          senha=d["usuario_senha"],
                          logado=d["usuario_logado"],
                          admin=d["usuario_admin"])
            usuarios.append(usuario)
        return usuarios

    def get_usuario(self, id):
        data = self.execute_query('''select * from usuario where usuario_id = {}'''.format(id))
        if len(data) < 1:
            return None
        usuarios = []
        for d in data:
            usuario = Usuario(
                id=d["usuario_id"],
                login=d["usuario_login"],
                senha=d["usuario_senha"],
                logado=d["usuario_logado"],
                admin=d["usuario_admin"])
            usuarios.append(usuario)
        return usuarios[0]

    def get_usuario_pelo_login(self, login):
        data = self.execute_query('''select * from usuario where usuario_login = {}'''.format(login))
        if len(data) < 1:
            return None
        usuarios = []
        for d in data:
            usuario = Usuario(
                id=d["usuario_id"],
                login=d["usuario_login"],
                senha=d["usuario_senha"],
                logado=d["usuario_logado"],
                admin=d["usuario_admin"])
            usuarios.append(usuario)
        return usuarios[0]
