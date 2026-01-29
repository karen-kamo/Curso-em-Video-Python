'''enunciado: desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.'''
d = float(input('Digite a distância em Km: '))
if d <= 200:
  custo = d * 0.5
else:
  custo = d * 0.45
print(f'O valor total será de R${custo:.2f}')