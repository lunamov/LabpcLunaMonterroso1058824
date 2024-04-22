lista = []
cantidad = 0

while cantidad < 5:
    edad = int(input("Ingrese una edad: "))
    if edad >= 0:
        lista.append(edad)
        cantidad += 1
    else:
        print("La edad no es válida")

print("Las edades ingresadas son:")
for edad in lista:
    print(edad)
