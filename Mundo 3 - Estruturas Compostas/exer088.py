'''enunciado: faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta'''
from random import randint
from time import sleep
quant = int(input('Quantos jogos você vai jogar? '))
jogos = []
for c in range(quant):
  jogo = []
  while len(jogo) != 6:
    palpite = randint(1, 60)
    if palpite not in jogo:
      jogo.append(palpite)
  jogos.append(jogo)
for pos, j in enumerate(jogos):
  j.sort()
  print(f'Jogo {pos+1}: {j}')
  sleep(0.7)