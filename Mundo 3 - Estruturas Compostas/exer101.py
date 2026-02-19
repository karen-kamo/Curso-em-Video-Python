'''enunciado: crie um programa que tenha uma função chamada votar() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições'''
from datetime import date
atual = date.today().year

def votar(nasc):
  idade = atual - nasc
  if idade >= 18:
    return 'OBRIGATÓRIO'
  elif 16 <= idade < 18:
    return 'OPCIONAL'
  elif idade < 16:
    return 'NEGADO'

nasc = int(input('Digite seu ano de nascimento: '))
print(votar(nasc))
