'''enunciado: faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado nçao tenha sido informado corretamente'''
def ficha(nome='<desconhecido>', gols=0):
  print('-' * 30)
  print(f'o jogador {nome} fez {gols} gols no campeonato.')
nome = str(input('Nome do jogador: ')).strip().title()
gols = str(input('Número de gols: '))
if gols.isnumeric():
  gols = int(gols)
else:
  gols = 0
if nome == '':
  ficha(gols=gols)
else:
  ficha(nome, gols)