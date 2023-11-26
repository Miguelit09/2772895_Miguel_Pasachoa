from cuadrado import Cuadrado

print("Primer cuadrado: ")
figura1 = Cuadrado(2)
print(f"El perimetro del cuadrado 1 es de {figura1.perimetro()}m")
print(f"El area del cuadrado 1 es de {figura1.area()} m2\n")

print("Segundo cuadrado: ")
figura2 = Cuadrado(4)
print(f"El perimetro del cuadrado 2 es de {figura2.perimetro()}m")
print(f"El area del cuadrado 2 es de {figura2.area()} m2\n")

print("Tercer cuadrado: ")
figura3 = Cuadrado(6)
print(f"El perimetro del cuadrado 3 es de {figura3.perimetro()}m")
print(f"El area del cuadrado 3 es de {figura3.area()} m2\n")

print("Cuarto cuadrado: ")
figura4 = Cuadrado(8)
print(f"El perimetro del cuadrado 4 es de {figura4.perimetro()}m")
print(f"El area del cuadrado 4 es de {figura4.area()} m2\n")

print("Actualizando lados:\nCuadrado 1:")
print(f"Lado actual: {figura1.lado}")
figura1.lado = 4
print(f"Nuevo lado: {figura1.lado}\n")

print("Cuadrado 2:")
print(f"Lado actual: {figura2.lado}")
figura2.lado = 8
print(f"Nuevo lado: {figura2.lado}\n")

print("Cuadrado 3:")
print(f"Lado actual: {figura3.lado}")
figura3.lado = 12
print(f"Nuevo lado: {figura3.lado}\n")

print("Cuadrado 4:")
print(f"Lado actual: {figura4.lado}")
figura4.lado = 16
print(f"Nuevo lado: {figura4.lado}")
