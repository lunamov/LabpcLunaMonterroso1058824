print("Semana No. 12: Ejercicio 1")
print("Menú", "a. Sumatoria", "b. Factorial", "c. Tablas de Multiplicar", "d. Número perfecto", sep="\n")
opcion = input("Ingrese su opción")

match opcion:
    case "a":

        n = int(input("Ingrese un número entero positivo"))
        if(n <= 0):
            print("Error, número debe ser mayor a cero")
        contador = 1
        sumatoria = 0
        while (contador <= n):
            sumatoria += contador
            contador += 1
        print(f"Sumatoria: {sumatoria}")

    case "b":

        n = int(input("Ingrese un número entero positivo"))
        if(n <= 0):
            print("Error, número debe ser mayor a cero")
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        print(f"Factorial: {factorial}")

    case "c":

        tituloCol = "\t" 
        for col in range(1, 11): 
            tituloCol += str(col) + "\t" 
        print (tituloCol)

        textoFila = ""
        for fila in range(1, 11):
            textoFila += str(fila) + "\t"

            for col in range(1, 11): 
                textoFila += str(fila*col) + "\t"

            print (textoFila)
            textoFila = ""
    
        