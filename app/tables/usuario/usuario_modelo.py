class Usuario:
    def __init__(self,
                 id=0,
                 login="none",
                 senha="none",
                 logado=0,
                 email="none",
                 confirmaemail=0,
                 perfil_id=0):
                    self.id = id
                    self.login = login
                    self.senha = senha
                    self.logado = logado
                    #self.email = email
                    #self.confirmaemail = confirmaemail
                    self.perfil_id = perfil_id

    def serializa(self):
        return {
                "id": self.id,
                "login": self.login,
                "senha": self.senha,
                "logado": self.logado,
                #"email": self.email ,
                #"confirmaemail": self.confirmaemail ,
                "perfil_id": self.perfil_id
                }
