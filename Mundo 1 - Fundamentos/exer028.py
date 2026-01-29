'''enunciado: escreva um programa que faça o computador pensar em um número entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random
nPc = random.randint(0, 5)
print('Estou pensando em um número entre 0 e 5...')
nJog = int(input('Adivinhe o número que eu escolhi: '))
if nJog == nPc:
  print('Parabéns! Você venceu.')
else:
  print(f'Hahaha, você perdeu, escolhi o {nPc}. Mais sorte na próxima!')