'''enunciado: crie um programa que gerencie o aproveitamente de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato'''
jogador = dict()
jogador['nome'] = str(input('Digite o nome: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
total = 0
gols = []
for c in range(partidas):
  n = int(input(f'Quantos gols na partida {c}? '))
  gols.append(n)
  total += n
jogador['gols'] = gols
jogador['total'] = total
print('-=' * 30)
for k, v in jogador.items():
  print(f'O campo {k} tem o valor {v}')

