#Exámen Corto 1 | Luna y Jorge
num = int(input("Ingresa un número entero positivo: "))

suma = 0
for i in range(1, num):
    if num % i == 0:
        suma += i

if suma == num:
    print(f"{num} es un número perfecto")
else:
    print(f"{num} no es un número perfecto")