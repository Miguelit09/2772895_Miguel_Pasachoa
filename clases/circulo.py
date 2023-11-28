from abstracta import Abstracta

class Circulo(Abstracta):
	PI = 3.1416
	def __init__(self,radio):
		self.radio = radio

	def perimetro(self):
		return 2*self.PI*self.radio

	def area(self):
		return self.PI * (self.radio**2)

