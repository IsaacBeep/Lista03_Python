#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas
dist = int(input('Qual a distancia que voce deseja percorrer em Km: '))

if dist <= 200:
    imp = (dist * 0.50) + dist
    print('Iremos cobrar um total de {} Reais'.format(imp))
else:
    imp = (dist * 0.45) + dist
    print('Iremos cobrar um total de {} Reais'.format(imp))