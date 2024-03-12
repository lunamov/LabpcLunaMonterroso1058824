print("Ejercicio 1: Operaciones aritméticas")
#entradas
numero1 = int(input("ingrese un número entero"))
numero2 = int(input("ingrese otro número entero"))
#operaciones
divisionEntera = numero1//numero2
divisionModular = numero1%numero2
suma = numero1+numero2
resta = numero1-numero2
multiplicacion = numero1*numero2
#salidas
print("Division entera:", divisionEntera)
print("Division modular:", divisionModular)
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)

# EJERCICIO 2

print("Ejercicio 2: Operaciones booleanas")

diferencia = numero1 != numero2
mayor = numero1 > numero2
menor = numero1 < numero2
igualdad = numero1 == numero2


print("número 1 es diferente que número 2:", diferencia)
print("número 1 mayor que número 2:", mayor)
print("número 1 menor que número 2:", menor)
print("número 1 es igual que número 2:", igualdad)

# EJERCICIO 3

print("Ejercicio 3: jerarquía de operadores")

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

respuesta1 = a * b + c
respuesta2 = a * (b + c)
respuesta3 = a * b + c
respuesta4 = 3 * a + 2 * b

print("a * b + c = ", respuesta1)
print("a * (b + c) =", respuesta2)
print("a * b + c =", respuesta3 )
print("3 * a + 2 * b =", respuesta4)