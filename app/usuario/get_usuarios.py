def get_usuarios(self):
	data = self.execute_query("select * from usuario")
	usuarios = []
	for u in data:
		usuario = Usuario(
			id=u["usuario_id"],
			login=u["usuario_login"],
			senha=u["usuario_senha"],
			logado=u["usuario_logado"],
			admin=u["usuario_admin"])
		usuarios.append(usuario)
	return usuarios
