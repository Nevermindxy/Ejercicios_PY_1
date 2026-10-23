#Contar vocales: Recorre una frase ingresada por el usuario y cuenta cuántas vocales contiene en total.Ejercicios con bucle while
vocales = ['a', 'e', 'i', 'o', 'u']
frase=input ("Introducir una frase para contar las vocales")
contador=0
posicion = 0
while posicion < len(frase):
    letra_actual = frase[posicion]
    if letra_actual in vocales:
        contador+=1
    posicion+=1
print("El total de vocales es:", contador)
   