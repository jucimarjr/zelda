import hashlib

class Criptografador():
    def gerar_hash(get_senha, salt):
        m = hashlib.md5()
        senha_salt = str(get_senha)
        m.update(senha_salt.encode('utf-8'))
        return m.hexdigest()
