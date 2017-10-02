def get_usuarios_logados(self):
	data = self.execute_query("select * from usuario\
		where usuario_logado = 1")
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