def cadastra_usuario(self, usuario):
	self.execute_query("insert into usuario (usuario_login, usuario_senha, usuario_logado, usuario_admin) values ('{}', '{}', '{}', '{}')".format(usuario.login, usuario.senha, usuario.logado, usuario.admin), True)
