from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views

from .features.funcionario_listar.funcionario_listar_front import funcionario_listar
from .features.funcionario_cadastrar.funcionario_cadastrar_front import funcionario_cadastrar
from .features.funcionario_editar.funcionario_editar_front import funcionario_editar
from .features.funcionario_remover.funcionario_remover_front import funcionario_desativar

from .features.setor_listar.setor_listar_front import setor_listar
from .features.setor_cadastrar.setor_cadastrar_front import setor_cadastrar
from .features.setor_editar.setor_editar_front import setor_editar
from .features.setor_remover.setor_remover_front import setor_desativar

from .features.usuario_listar.usuario_listar_front import usuario_listar
from .features.usuario_cadastrar.usuario_cadastrar_front import usuario_cadastrar
from .features.usuario_editar.usuario_editar_front import usuario_editar
from .features.usuario_remover.usuario_remover_front import usuario_remover