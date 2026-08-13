class Botao:
	def __init__(self, cor, nome, tamanho):
		self.cor = cor
		self.nome = nome
		self.tamanho = tamanho
		
	def trocar_cor(self, cor):
		self.cor = cor
		print("Nova cor adicionada: ", cor)
	
class Input_text(Botao):
	def __init__(self, cor, nome, tamanho, tipo):
		super().__init__(cor, nome, tamanho)
		self.tipo = tipo
		