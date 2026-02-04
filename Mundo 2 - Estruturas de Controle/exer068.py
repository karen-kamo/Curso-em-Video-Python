'''enunciado: faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''
from random import randint
vit = 0
print('Vamos jogar um ÍMPAR OU PAR?')
while True:
  #Escolha do ímpar ou par
  escolha = str(input('Escolha ÍMPAR ou PAR: ')).strip().upper()[0]
  if escolha in 'ÍI':
    com = 2
    jog = 1
    print('Sou PAR!')
  elif escolha in 'PAR':
    com = 1
    jog = 2
    print('Sou ÍMPAR!')
  
  #Escolha dos números
  print('Vamos falar nossos números agora...')
  nCom = randint(0, 10)
  nJog = int(input('Meu número é: '))
  print(f'Eu escolho {nCom}!')
  soma = nCom + nJog

  #Possíveis rotas
  if (jog == 1 and soma % 2 != 0) or (jog == 2 and soma % 2 == 0):
    print('Você venceu! Vamos de novo')
    vit += 1
    print('-' * 30)
  else:
    print('Você perdeu. Hahaha')
    break
print(f'Você me venceu {vit} vezes')



  

