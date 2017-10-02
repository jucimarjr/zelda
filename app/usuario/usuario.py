from app.usuario import cadastra_usuario, get_usuarios, get_usuarios_logados, get_usuarios_admin, edita_usuario, deleta_usuario, serializa

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
			
	def serializa(self):
		return serializa(self)
		
	# CRUD - USUARIO		

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

