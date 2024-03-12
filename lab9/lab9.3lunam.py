print("Ejercicio 1: Operaciones aritméticas")

#entradas
name= input(("ingrese su nombre"))
numero2 = int(input("ingrese su número de carnet"))
numero1 = int(input("ingrese una cantidad en metros"))

#operaciones

# Convertir a millas
millas = numero1 / 1609
# Convertir a kilómetros
kilometros = numero1 / 1000
# Convertir a pies
pies = numero1 * 3.28
# Convertir a pulgadas
pulgadas = pies * 12

#salidas
print(name)
print(numero2)

print("ingrese un número:",  numero1)
print("resultado:")
print("Distancia en millas: ", millas)
print("Distancia en kilómetros: ", kilometros)
print("Distancia en pies: ", pies)
print("Distancia en pulgadas:", pulgadas)