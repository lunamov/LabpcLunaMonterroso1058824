print("Semana No.10: Ejercicio 1")
mesEntrada = int(input("Ingrese un número del 1 al 12"))
mesSalida = ""
match mesEntrada:
    case 1:
        mesSalida = "Enero"
    case 2:
        mesSalida = "Febrero"
    case 3:
        mesSalida = "Marzo"
    case 4:
        mesSalida = "Abril"
    case 5:
        mesSalida = "Mayo"
    case 6:
        mesSalida = "Junio"
    case 7:
        mesSalida = "Julio"
    case 8:
        mesSalida = "Agosto"
    case 9:
        mesSalida = "Septiembre"
    case 10:
        mesSalida = "Octubre"
    case 11:
        mesSalida = "Noviembre"
    case 12:
        mesSalida = "Diciembre"
    case _:
        mesSalida = "Número inválido"
print("Mes:", mesSalida)




print("Semana No.10: Ejercicio 2")
a = int(input("Ingrese un número mayor a 0: "))
b = int(input("Ingrese un número mayor a 0: "))
c = int(input("Ingrese un número mayor a 0: "))

if a <= 0 or b <= 0 or c <= 0:
   print("ERROR, tiene que ser mayor a 0")
else:
   if a > b:
       if a > c:
           print("A es mayor que B y C")
       else:
           if a == c:
               print("C es mayor que B y A es igual a C")
           else:
               print("C es mayor que B y A y A es diferente a C")
   else:
       if b > c:
           print("B es mayor que A y C")
       else:
           if a == b:
               print("A es igual a B y ambos son mayores que C")
           else:
               print("C es mayor que A y B")



    
print("Semana No.10: Ejercicio 3")

dia = int(input("Ingrese el día de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento (1-12): "))
ano = int(input("Ingrese el año de nacimiento: "))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    signo = "Aries"
elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 21):
    signo = "Tauro"
elif (mes == 5 and dia >= 22) or (mes == 6 and dia <= 21):
    signo = "Géminis"
elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
    signo = "Leo"
elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 23):
    signo = "Virgo"
elif (mes == 9 and dia >= 24) or (mes == 10 and dia <= 23):
    signo = "Libra"
elif (mes == 10 and dia >= 24) or (mes == 11 and dia <= 22):
    signo = "Escorpio"
elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
    signo = "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
    signo = "Capricornio"
elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
    signo = "Acuario"
elif (mes == 2 and dia >= 20) or (mes == 3 and dia <= 20):
    signo = "Piscis"
else:
    signo = "Fecha de nacimiento inválida"

print(f"Tu signo zodiacal es: {signo}")