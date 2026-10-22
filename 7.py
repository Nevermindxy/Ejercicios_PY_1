final_lista = int(input("Escriba hasta donde quiere que llegue la lista de números enteros: "))


lista_numeros = list(range(1, final_lista + 1,2))
print("La lista es:", lista_numeros)
suma_total = 0
for numero in lista_numeros:
    suma_total += numero

print("La suma total es:", suma_total)