from ...cursor import db

class Sistema:

	def __init__(self, sistema_id = None):
		
		self.__sistema_id = None
		self.nome = None
		self.desc = None
		self.__status = 0
		self.prefixo = None

		if sistema_id is not None:
			data = db.get_sistema(sistema_id)
			if data is not None:
				self.__sistema_id = sistema_id
				self.nome = data['sistema_nome']
				self.desc = data['sistema_desc']
				self.__status = data['sistema_status']
				self.prefixo = data['sistema_prefixo']


	def get_id(self):
		return self.__sistema_id

	def get_status(self):
		return self.__status
	
	def get_status_texto(self):
		if self.__status == 0:
			return 'Ativado'
		elif self.__status == 1:
			return 'Desativado'
		
		return 'Indefinido'

	def desativa(self):
		if self.__status == 0:
			self.__status = 1
			db.desativa_sistema(self.get_id())

	def ativa(self):
		if self.__status == 1:
			self.__status = 0
			db.ativa_sistema(self.get_id())

	def salva(self):
		if self.__sistema_id is not None:
			db.edita_sistema(self)
		else:
			self.__sistema_id = db.cadastra_sistema(self)