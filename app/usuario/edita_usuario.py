def edita_usuario(self, usuario):
	self.execute_query("update usuario set usuario_login = '{}', usuario_senha = '{}', usuario_admin = '{}' where usuario_id = '{}'".format(usuario.login, usuario.senha, usuario.admin, usuario.id), True)
