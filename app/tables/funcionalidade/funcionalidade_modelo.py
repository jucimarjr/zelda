class Funcionalidade:
    def __init__(self,
                 funcionalidade_id=0,
                 funcionalidade_codigo= None,
                 funcionalidade_nome=None,
                 funcionalidade_desc=None,
                 funcionalidade_caminho=None,
                 funcionalidade_caminho_imagem=None,
                 funcionalidade_status=0,
                 sistema_id=0):
         self.funcionalidade_id=funcionalidade_id
         self.funcionalidade_codigo=funcionalidade_codigo
         self.funcionalidade_nome= funcionalidade_nome
         self.funcionalidade_desc=funcionalidade_desc
         self.funcionalidade_caminho=funcionalidade_caminho
         self.funcionalidade_caminho_imagem=funcionalidade_caminho_imagem
         self.funcionalidade_status=funcionalidade_status
         self.sistema_id=sistema_id

    def serializa(self):
        return {
                "funcionalidade_id":  self.funcionalidade_id,
                "funcionalidade_codigo": self.funcionalidade_codigo,
                "funcionalidade_nome":  self.funcionalidade_nome,
                "funcionalidade_desc" : self.funcionalidade_desc,
                "funcionalidade_caminho" :  self.funcionalidade_caminho,
                "funcionalidade_caminho_imagem" :  self.funcionalidade_caminho_imagem,
                "funcionalidade_status" :  self.funcionalidade_status,
                "sistema_id" : self.sistema_id
                }