print("Semana No. 11: Ejercicio 1")
n = int(input("Ingrese un número mayor 0"))

if (n <= 0 ):
    print("error, el número es menor a 0")
a = 0
b = 1
c = 0
i = 2
resultado = ""

if (n>0):
    resultado = str(a)

    if (n>1):
        resultado = resultado + "," + str(b)
    while (i < n):
        c = a + b
        resultado = resultado + "," + str(c)
        a=b
        b=c
        i= i + 1

    print(resultado)

# EJERCICIO 2 LUNA
    
    print("Semana No. 11: Ejercicio 2")

n2 = int(input("Ingrese un número mayor  0"))

if (n2 <= 0 ):
    print("error, el número es menor a 0")

    #A
calculoA= 0
for xA in range (1, n2 + 1):
    calculoA += 1 / xA
print ("El resultado de A es", calculoA)

    #B

calculoB = 0
for xB in range(1, n+1):
            calculoB += 1/(2**xB)
print ("El resultado de B es", calculoB)

  #C 
x = int(input("Ingrese un número entero positivo para x: "))
a = int(input("Ingrese un número entero positivo para a: "))
calculoC = 0
for xC in range(1, n+1):
            calculoC += x**(xC) * a**(n-xC)
print ("El resultado de C es", calculoC)