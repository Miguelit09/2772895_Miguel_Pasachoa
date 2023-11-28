from abstracta import Abstracta

class Cuadrado(Abstracta):
	def __init__(self,lado):
		self.__lado = lado

	def perimetro(self):
		return self.__lado*4

	def area(self):
		return self.__lado**2
	@property
	def lado(self):
		return self.__lado

	@lado.setter
	def lado(self, nuevo_lado):
		self.__lado = nuevo_lado


