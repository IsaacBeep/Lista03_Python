#Peça ao usuário para inserir um número entre 10 e 20 (inclusive). Se ele inserir um número dentro desse intervalo, exiba a mensagem "Obrigado", caso contrário, exiba a mensagem "Resposta incorreta".
numero = int(input('Digite um numero entre 10 e 20: '))

if numero >=10:
    print('Obrigado')

elif numero <=20:
    print('Obrigado')

else:
    print('Resposta incorreta')