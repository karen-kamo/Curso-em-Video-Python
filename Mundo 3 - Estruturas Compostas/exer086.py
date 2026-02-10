'''enunciado: crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre na tela, com a formatação correta.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
  for c in range(0, 3):
    n = int(input(f'Valor da posição {l} x {c}: '))
    matriz[l][c] = n 

for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{matriz[l][c]}]', end='')
  print()
