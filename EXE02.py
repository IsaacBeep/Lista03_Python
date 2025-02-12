#Peça ao usuário para inserir um número inferior a 20. Se ele inserir um número 20 ou mais, exiba a mensagem "Muito alto", caso contrário, exiba "Obrigado".
numero = int(input('Digite numero inferior a 20: '))

if numero >= 20:
    print('Muito alto')
else:
    print('obrigado')