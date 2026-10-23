#Menú interactivo: Diseña un bucle while que muestre un menú de opciones y se repita de manera indefinida hasta que el usuario introduzca la opción de salir.
while True:
    print("\nMENU ")
    print("1. Saludar")
    print("2. Mostrar creditos")
    print("3. Salir")
    opcion=int(input("Introducir la opcion que quiere escoger"))
    if opcion==1:
        print('Hola, como estas?')
    elif opcion==2:
        print('Este programa fue hecho por: Emilio Garcia')
    elif opcion==3:
        print('Gracias por usar el programa, adios!!!')
        break
    else:
        print("Opcion no valida. Por favor, intenta de nuevo.")