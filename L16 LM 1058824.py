#Semana No. 16 Ejercicio 1
import random
print("Semana No. 16 Ejercicio 1")

lista = []
for x in range(10):
    lista.append(random.randint(0,10))

opcion = "a"

while(opcion != "e"):
    print("Menú")
    print("a. mostrar números", "b. promedio", "c. longitud", "d. Posición", "e. ejercicio 2")
    opcion = input("Ingrese su opción: ")

    match opcion:
        case "a":
            for x in range (len(lista)):
                print(f"No. {x}: {lista[x]}")

        case "b":
            sumatoria = 0
            for x in range (len(lista)):
                sumatoria += lista[x]
                promedio= sumatoria/len(lista)
            print(f"promedio:", {promedio})
                

        case "c":
            print("La longitud es: ", len(lista))

        case "d":
            suma_pares = sum(lista[i] for i in range(len(lista)) if i % 2 == 0)
            suma_impares = sum(lista[i] for i in range(len(lista)) if i % 2 != 0)
            print(f"La suma de posiciones pares es: {suma_pares}")
            print(f"La suma de posiciones impares es: {suma_impares}")

print("Semana No. 16 Ejercicio 2") 

cantFilas= int(input("Ingrese la cantidqad de filas"))
cantCols= int(input("Ingrese la cantidqad de Cols"))

matriz = [[0 for x in range(cantCols)]for y in range(cantFilas)]

for xFilas in range (cantFilas):
    for xCols in range (cantCols):
        matriz[xFilas][xCols]= random.randint(0,1000)
print(matriz)

numeros = [num for fila in matriz for num in fila] 
pares = sum(1 for num in numeros if num % 2 == 0)
impares = sum(1 for num in numeros if num % 2 != 0)
mayor = max(numeros)
menor = min(numeros)


print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")