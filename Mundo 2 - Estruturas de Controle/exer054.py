'''enunciado: crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''
from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
  nasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
  idade = atual - nasc
  if idade >= 18:
    maiores += 1
  else:
    menores += 1
print(f'Maiores: {maiores}. Menores: {menores}')