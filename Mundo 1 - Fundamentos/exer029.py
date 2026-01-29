'''enunciado: escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
v = float(input('Digite a velocidade do carro: '))
if v >= 80:
  custo = (v - 80) * 7
  print(f'Você foi multado! O valor da sua multa é de R${custo:.2f}')
else:
  print('Você não foi multado.')