'''enunciado: crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla'''
from random import randint
nums = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = 0
for pos, n in enumerate(nums):
  if pos == 0:
    maior = n
    menor = n
  else:
    if n > maior:
      maior = n
    elif n < menor:
      menor = n
print(f'Lista: {nums}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')