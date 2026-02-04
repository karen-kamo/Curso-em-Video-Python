'''enunciado: melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''
from random import randint
print('Vou pensar em um número...')
com = randint(0, 10)
print('Tente adivinhar!')
jog = int(input('Qual o seu palpite de 0 a 10? '))
while jog != com:
  if jog > com:
    print(f'É menos que {jog}...')
  elif jog < com:
    print(f'É mais que {jog}...')
  jog = int(input('Qual o seu palpite? '))
print(f'Você acertou! Era {com}')