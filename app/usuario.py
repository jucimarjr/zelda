class Usuario:
    def __init__(self,
                 id=0,
                 login="none",
                 senha="none",
                 logado=1,
                 admin=1):
                   self.id = id
                   self.login = login
                   self.senha = senha
                   self.logado = logado
                   self.admin = admin
        

    def __str__(self):
        string = "{"
        string += "id:" + str(self.id) + ","
        string += "login:" + self.login + ","
        string += "senha:" + self.senha + ","
        string += "logado:" + str(self.logado) + ","
        string += "admin:" + str(self.admin) + ","
        string += "}"

        return string

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
	usuario = Usuario()
	print(usuario)