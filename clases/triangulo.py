class Triangulo:
	def __init__(self,lado1,lado2,lado3,altura):
		self.lado1  = lado1
		self.lado2  = lado2
		self.lado3  = lado3
		self.altura = altura
		self.base = lado2

	def perimetro(self):
		return (self.lado1+self.lado2+self.lado3)

	def area(self):
		return (self.base*self.altura)/2


