from flask_mysqldb import MySQL

class DocumentoInterface():

	def __init__(self, app):
		self.mysql = MySQL(app)

	def execute_query(self, query, insert = False):
		cur = self.mysql.connection.cursor()
		cur.execute(query)
		if insert:
			self.mysql.connection.commit()
		else:
			data = cur.fetchall()
			cur.close()
			if len(data) < 1:
				return None
			return data

	def get_documento(self, documento_id):
		data = self.execute_query("select * from documento where documento_id = '{}' limit 1".format(documento_id))
		return data[0]

	def get_documento_ids(self):
		data = self.execute_query("select * from documento")
		return data

	def cadastra_documento(self, documento):
		self.execute_query("insert into documento(documento_id, documento_tipo, documento_desc, documento_status)\
		 values ('{}', '{}', '{}', '{}')".format(documento.id, documento.tipo, documento.desc, documento.get_status()), True)
		data = self.execute_query("select LAST_INSERT_ID() as last from documento")
		return data[0]['last']

    #def edita_documento_caminho_foto(self, documento):
        #self.execute_query("update documento set documento_caminho_foto = '{}' where documento_id = '{}'".format(documento.get_caminho_foto(), documento.get_id()), True)

	def edita_documento(self, documento):
		self.execute_query("update documento set documento_id = '{}', documento_tipo = '{}' where documento_id = '{}'".format(documento.id, documento.tipo, documento.get_id()), True)

	def desativa_documento(self, documento_id):
		self.execute_query("update documento set documento_status = 1 where documento_id = '{}'".format(documento_id), True)

	def ativa_documento(self, documento_id):
		self.execute_query("update documento set documento_status = 0 where documento_id = '{}'".format(documento_id), True)