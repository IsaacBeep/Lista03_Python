#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. (usar ELIF)
num = int(input('Digite o 1 numero: '))
num2 = int(input('Digitw o 2 numero: '))
fac = input('Agora escolha o metodo: soma (+), subtração (-), multiplicação (*) e divisão (/): ')

if fac == '+':
    soma = num + num2
    print('{}'.format(soma))

elif fac == '-':
    sub = num - num2
    print('{}'.format(sub))

elif fac == '*':
    mult = num * num2
    print('{}'.format(mult))

elif fac == '/':
    div = num / num2
    print('{}'.format(div))

else:
    print('Isso não é um numero')