class Semaforo(object):

	estado = False
	num_carros = 0
	t_medio_espera = 0

	def __init__(self):
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