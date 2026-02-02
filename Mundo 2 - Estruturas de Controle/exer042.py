'''enunciado: refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: escaleno, isósceles ou equilátero'''
r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  if r1 == r2 == r3:
    print('Forma um triângulo EQUILÁTERO')
  elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Forma um triângulo ISÓSCELES')
  else:
    print('Forma um triângulo ESCALENO')
else:
  print('Não forma um triângulo')