#Cálculo de factorial: Solicita un número entero positivo al usuario y calcula su factorial utilizando un contador y un bucle while.
num=int(input('introducir un numero entero positivo'))
factorial=1
contador=1
while contador<=num:
    factorial*=contador
    contador+=1
print(f"El factorial de {num} es: {factorial}")