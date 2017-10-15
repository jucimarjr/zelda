from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_json import FlaskJSON, json_response, as_json
from flask_mysqldb import MySQL

from app.db_interface import Zelda
from app.tables.funcionario.funcionario_modelo import Funcionario
from app.tables.usuario.usuario_modelo import Usuario
from app.tables.setor.setor_modelo import Setor

from webservice import app

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'zelda'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

api = Api(app)
json = FlaskJSON(app)
db = Zelda(app)

app.config['JSON_ADD_STATUS'] = False

# Define os argumentos recebidos seja por parâmetros de url ou dados via post
parser = reqparse.RequestParser()

parser.add_argument('funcionario_nome')
parser.add_argument('funcionario_id')
parser.add_argument('funcionario_situacao')

parser.add_argument('setor_id')
parser.add_argument('setor_pai')
parser.add_argument('setor_nome')
parser.add_argument('setor_situacao')

parser.add_argument('usuario_id')
parser.add_argument('usuario_login')
parser.add_argument('usuario_senha')


# Requisições para um funcionário
class Funcionario(Resource):

    # Lista um funcionário por id
    def get(self, func_id):
        return jsonify(db.get_funcionario(func_id).serializa())

    # Edita funcionário por id
    def put(self, func_id):
        args = parser.parse_args()

        funcionario = Funcionario(id = func_id,
            nome = args['funcionario_nome'],
            situacao = args['funcionario_situacao'])

        db.edita_funcionario(funcionario)
        return jsonify(funcionario.serializa())

api.add_resource(Funcionario, '/funcionario/<int:func_id>')


# Requisição para todos os funcionários
class Funcionarios(Resource):

    # Lista todos os funcionários
    def get(self):
        return jsonify([func.serializa() for func in db.get_funcionarios()])

api.add_resource(Funcionarios, '/funcionario')


# Requisição para um setor
class Setor(Resource):

    # Lista um setor por id
    def get(self, setor_id):
        return jsonify(db.get_setor(setor_id).serializa())

    # Edita setor por id
    def put(self, setor_id):
        args = parser.parse_args()

        setor = Setor(id = setor_id,
            nome = args['setor_nome'],
            situacao = args['setor_situacao'],
            setor_pai = args['setor_pai'])

        db.edita_setor(setor)
        return jsonify(setor.serializa())

api.add_resource(Setor, '/setor/<int:setor_id>')


# Requisição para todos os setores
class Setores(Resource):

    # Lista todos os setores
    def get(self):
        return jsonify([setor.serializa() for setor in db.get_setores()])

api.add_resource(Setores, '/setor')


# Requisição para um usuário
class Usuario(Resource):

    # Lista um usuário por id
    def get(self, user_id):
        return jsonify(db.get_usuario(user_id).serializa())

    # Edita usuário por id
    def put(self, user_id):
        args = parser.parse_args()

        usuario = Usuario(id = user_id,
            login = args['usuario_login'],
            senha = args['usuario_senha'])

        db.edita_usuario(usuario)
        return jsonify(usuario.serializa())

api.add_resource(Usuario, '/usuario/<int:user_id>')


# Requisição para todos os usuários
class Usuarios(Resource):

    # Lista todos os usuários
    def get(self):
        return jsonify([u.serializa() for u in db.get_usuarios()])

api.add_resource(Usuarios, '/usuario')
