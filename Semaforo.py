class Semaforo(object):
	num_carros = 0
	t_medio_espera = 0

	def __init__(self, estado):
		self.estado = estado
		self.num_carros = 0
		self.t_medio_espera = 0

	def mudaEstado(self):
		if self.estado == True:
			self.estado = False
		else:
			self.estado = True

	def tempoMedio(self, tempo):
		if self.t_medio_espera == 0:
			self.t_medio_espera = tempo
		else:
			self.t_medio_espera = (self.t_medio_espera + tempo)/2

	def addNumCarros(self):
		self.num_carros += 1

	def getNumCarros(self):
		return self.num_carros

	def getT_Medio_Espera(self):
		return self.t_medio_espera

	def getEstado(self):
		return self.estado

	def estaVazio(self):
		return self.num_carros <= 0

	def removeCarro(self):
		if self.num_carros > 0:
			self.num_carros = self.num_carros - 4