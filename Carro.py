#Objeto Carro

class Carro(object):

	def __init__(self):
		self.entrada = time.time()

	def getEntrada(self):
		return self.entrada

	def getSaida(self):
		return self.saida

	def setSaida(self):
		self.saida = time.time()