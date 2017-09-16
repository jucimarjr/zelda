import hashlib

# Classe que faz a criptografia da senha
class Criptografador():
    def gerarHash(getsenha, salt):
        m = hashlib.md5()
        senhaSalt = getsenha
        m.update(senhaSalt.encode('utf-8'))
        return m.hexdigest() 
