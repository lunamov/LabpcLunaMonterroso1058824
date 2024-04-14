#PROYECTO LUNA Y JORGE :)
nombre_cliente = input("Ingrese su nombre: ")
nit = input("Ingrese su NIT (si no desea, escribir not): ")
if not nit:
    nit = "CF"

licuado = "fresa con leche deslactosada sin azúcar"
tamaño = "normal"
precio = 20.0
azúcar = 0

# MENÚ CON OPCIONES :O

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Ver información del pedido")
    print("2. Agregar azúcar")
    print("3. Modificar leche")
    print("4. Agrandar")
    print("5. Confirmar")
    print("6. Salir")

# INFO DEL PEDIDO
    
def mostrar_info_pedido():
    print("\nInformación del pedido:")
    print("Nombre del cliente:", nombre_cliente)
    print("NIT:", nit)
    print("Licuado:", licuado)
    print("Tamaño:", tamaño)
    print("Azúcar:", azúcar)
    print("Precio:", precio)

# AZÚCAR
    
def agregar_azucar(azucar, precio):
    if azucar < 2:
        azucar += 1
        precio += 0.5
        print("\nSe agregó 1 cucharadita de azúcar.")
        print("Azúcar actual:", azucar)
        print("Precio actualizado:", precio)
    else:
        print("\nNo se puede agregar más azúcar.")
    return azucar, precio

# LECHE

def modificar_leche(licuado, precio):
    print("\nSeleccione el tipo de leche:")
    print("1. Sin leche (agua)")
    print("2. Leche deslactosada")
    print("3. Leche entera")
    print("4. Leche de soya")
    opcion_leche = int(input("Ingrese su opción: "))
    if opcion_leche == 1:
        licuado = "fresa sin leche (agua)"
        precio = 18.0
    elif opcion_leche == 2:
        licuado = "fresa con leche deslactosada sin azúcar"
        precio = 20.0
    elif opcion_leche == 3:
        licuado = "fresa con leche entera sin azúcar"
        precio = 22.0
    elif opcion_leche == 4:
        licuado = "fresa con leche de soya sin azúcar"
        precio = 22.0
    else:
        print("Opción inválida.")
    return licuado, precio

# AGRANDAR

def agrandar(tamaño, precio):
    if tamaño == "normal":
        tamaño = "grande"
        precio *= 1.05
        print("\nEl licuado se ha agrandado a tamaño grande.")
        print("Precio actualizado:", precio)
    else:
        print("\nEl licuado ya está en tamaño grande.")
    return tamaño, precio

# CONFIRMAR :))
def confirmar_pedido():
    mostrar_info_pedido()
    print("\nGracias por ordenar. :)")

# CONDICIONES DE LAS OPCIONES
while True:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        mostrar_info_pedido()
    elif opcion == 2:
        azúcar, precio = agregar_azucar(azúcar, precio)
    elif opcion == 3:
        licuado, precio = modificar_leche(licuado, precio)
    elif opcion == 4:
        tamaño, precio = agrandar(tamaño, precio)
    elif opcion == 5:
        confirmar_pedido()
        break
    elif opcion == 6:
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

