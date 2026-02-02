'''enunciado: crie um programa que faça o computador jogar jokenpô com você'''
import random
nome = str(input('Digite seu nome: ')).strip().title()

print(f'{nome}, vamos jogar um Jokenpô?')
print('=' * 30)
comp = random.randint(1, 3)

print('''[1] Pedra
[2] Papel
[3] Tesoura''')
jogador = int(input('Digite a sua opção: '))

if comp == 1:
  compJog = 'PEDRA'
elif comp == 2:
  compJog = 'PAPEL'
elif comp == 3:
  compJog = 'TESOURA'

if jogador == 1:
  jogadorJog = 'PEDRA'
elif jogador == 2:
  jogadorJog = 'PAPEL'
elif jogador == 3:
  jogadorJog = 'TESOURA'

print(f'Você escolheu {jogadorJog}')
print(f'Eu escolhi {compJog}')

if (comp == 1 and jogador == 3) or (comp == 2 and jogador == 1) or (comp == 3 and jogador == 2):
  print('Haha, ganhei!')
elif (jogador == 1 and comp == 3) or (jogador == 2 and comp == 1) or (jogador == 3 and comp == 2):
  print('Acho que você venceu... parabéns')
else:
  print('Empatamos! Vamos de novo')
