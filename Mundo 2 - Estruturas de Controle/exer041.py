'''enunciado: a Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade'''
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
if idade <= 9:
  print('MIRIM')
elif idade > 9 and idade <= 14:
  print('INFANTIL')
elif idade > 14 and idade <= 19:
  print('JUNIOR')
elif idade > 19 and idade <= 25:
  print('SÊNIOR')
else:
  print('MASTER')