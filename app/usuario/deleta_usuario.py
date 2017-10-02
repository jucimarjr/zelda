def deleta_usuario(self, usuario_id):
	self.execute_query("delete from usuario where usuario_id = '{}'".format(usuario_id), True)
