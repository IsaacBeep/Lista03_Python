#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal
din = int(input('Qual o valor do seu salario: '))

if din <= 2259.20:
    print('Nada')

elif din >= 2259.21 and din <= 2826.65:
    imposto = din * 0.075
    print('Imposto de renda de {}'.format(imposto))

elif din >= 2826.66 and din <= 3751.05:
    imposto = din * 0.150
    print('Imposto de renda de {}'.format(imposto))

elif din >= 3751.06 and din <= 4664.68:
    imposto = din * 0.220
    print('Imposto de renda de {}'.format(imposto))

else:
    imposto = din * 0.275
    print('Imposto de renda de {}'.format(imposto))