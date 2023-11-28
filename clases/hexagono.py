from abstracta import Abstracta

class Hexagono(Abstracta):
	# Lados es una lista con los 6 lados de la figura
	def __init__(self,lados,apotema):
		self.lados = lados
		self.apotema = apotema

	def perimetro(self):
		return sum(self.lados)

	def area(self):
		self.perimetro = sum(self.lados)
		return (self.perimetro*self.apotema)/2
