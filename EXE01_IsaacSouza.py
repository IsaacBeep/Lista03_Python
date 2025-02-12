#Peça dois numeros, se o primeiro numero for maior que o segundo exiba primeiro o 2 numero caso contrario mostre o 1 numero
numero = int(input('Digite o 1 numero: '))
numero2 = int(input('Digite o 2 numero: '))

if numero > numero2:
    print(numero)
    print(numero2)
elif numero2 > numero:
    print(numero2)
    print(numero)
else:
    print("errro")