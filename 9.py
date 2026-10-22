#Tabla de multiplicar: Dado un número entero, imprime su tabla de multiplicar del 1 al 10 utilizando un bucle for.
num=int(input("introducir un numero entero "))
for i in range(1,11):
    resultado=i * num
    print(f"{num} x {i} = {resultado}")