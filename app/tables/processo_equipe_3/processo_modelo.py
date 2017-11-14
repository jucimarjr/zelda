from ...cursor import db

class Processo:

	def __init__(self):

		self.processo_nome_aluno = None
		self.processo_id = None
		self.processo_tipo = None
		self.processo_descricao = None
		self.processo_link = None

	def salvar(self):
		db.salva_processo(self.processo_nome_aluno ,self.processo_tipo, self.processo_descricao)

	def get_processos(self):
		return db.get_processos()

	def edit(self):
		db.edit(self.processo_nome_aluno ,self.processo_tipo, self.processo_descricao, self.processo_id)

	def deletar(self):
		db.deletar(self.processo_id)