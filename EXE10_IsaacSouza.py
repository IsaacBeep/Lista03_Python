#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
sal = int(input('Qual seu salario: '))

if sal > 1250.00:
    aumen = (sal * 0.10) + sal
    print('Seu salario aumentou em {} Reais'.format(aumen))
else:
    aumen = (sal * 0.15) + sal
    print('Seu salario aumentou em {} Reais'.format(aumen))