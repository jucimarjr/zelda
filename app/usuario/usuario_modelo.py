class Usuario:
    def __init__(self,
                 id=0,
                 login="none",
                 senha="none",
                 logado=0,
                 admin=0):
                    self.id = id
                    self.login = login
                    self.senha = senha
                    self.logado = logado
                    self.admin = admin

    def serializa(self):
        return {
                "id": self.id,
                "login": self.login,
                "senha": self.senha,
                "logado": self.logado,
                "admin": self.admin
                }
