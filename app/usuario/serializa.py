def serializa(self):
	return {
		"id": self.id,
		"login": self.login,
		"senha": self.senha,
		"logado": self.logado,
		"admin": self.admin
		}
