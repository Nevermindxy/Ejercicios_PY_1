#Adivinar el número: Crea un programa con un número secreto fijo; el bucle while debe pedir intentos al usuario e indicarle si el número secreto es mayor o menor hasta que acierte.
num_secreto_jetsito=5

num_pachita=int(input('Introducir el numero que quiere adivinar'))
while num_pachita!=num_secreto_jetsito:
    if num_pachita<num_secreto_jetsito:
        print(f"el numero {num_pachita} es menor que el numero secreto")
    elif num_pachita>num_secreto_jetsito:
        print(f"el numero {num_pachita} es mayor que el numero secreto")
    num_pachita = int(input('Intenta de nuevo: '))
print("Felicidades, el numero secreto era 5!!!")