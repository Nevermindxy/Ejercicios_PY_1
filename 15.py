#Suma hasta número negativo: Pide números al usuario de forma repetida hasta que introduzca un número negativo, momento en el cual el bucle terminará y mostrará la suma acumulada de los valores ingresados.
contador=0
num=int(input('introducir un numero si introduce un numero negativo el programa termina y le dara la suma de los numeros introducidos'))
    
while num>=0:
    contador+=num
    num=int(input('introducir un numero'))
print(f"La suma total de los numeros positivos es: {contador}")
