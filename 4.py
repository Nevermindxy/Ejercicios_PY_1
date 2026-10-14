#PIDE UN NUMERO ENTERO AL USUARIO E INDICA MEDIANTE UN MENSAJE SI EL NUMERO INGRESADO EN PAR O IMPAR
num_entero=int(input('introducir un numero ENTERO'))
if num_entero%2==0:
    print(f"{num_entero} es par")
else:
    print(f'{num_entero} es impar')