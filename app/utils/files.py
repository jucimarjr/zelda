import os

from werkzeug import secure_filename
from app import ALLOWED_EXTENSIONS
from flask import flash

def get_extensao(nome_arquivo):
    return nome_arquivo.rsplit('.', 1)[1].lower()

def arquivo_permitido(nome_arquivo):
    return '.' in nome_arquivo and get_extensao(nome_arquivo) in ALLOWED_EXTENSIONS

def upload(caminho, arquivo_input, id_registro):
    nome_arquivo = get_nome_arquivo(arquivo_input)

    if arquivo_permitido(nome_arquivo):

        nome_final = monta_nome(id_registro, nome_arquivo)

        path = os.path.abspath(os.path.join(caminho, nome_final))

        arquivo_input.save(path)

        return nome_final
    else:

        return None

def get_nome_arquivo(arquivo_input):
    filename = secure_filename(arquivo_input.filename)
    return filename

def monta_nome(id_arquivo, nome_arquivo):
    return str(id_arquivo) + '.' + nome_arquivo.rsplit('.', 1)[1]

def flash_errors_extensao():
    str = 'Os formatos são restritos a '
    for i in range(0, len(ALLOWED_EXTENSIONS)):
        if i != len(ALLOWED_EXTENSIONS) - 1:
            str = str + ', '
        else:
            str = str + ' e '
        str = str + ALLOWED_EXTENSIONS[i]
    return str
