'''enunciado: faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo de alismento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc
print(f'Idade: {idade}')
if idade < 18:
  print(f'Ainda falta {18 - idade} anos para se alistar')
elif idade == 18:
  print('Já está na hora de se alistar.')
else:
  print(f'Já passou {idade - 18} anos. Se aliste já!')