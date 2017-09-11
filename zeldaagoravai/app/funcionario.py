class Funcionario:

  def __init__(self,
               id=0,
               nome="none",
               login="none",
               situacao="none",
               setor_id="none",
               setor_nome="none",
               setor_situacao=0,
               senha="none"):
    self.id = id
    self.nome = nome
    self.login = login
    self.situacao = situacao
    self.setor_id = setor_id
    self.setor_nome = setor_nome
    self.setor_situacao = setor_situacao
    self.senha = senha    
