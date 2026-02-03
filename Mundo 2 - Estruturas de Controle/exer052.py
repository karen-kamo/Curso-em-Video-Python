'''enunciado: faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''
n = int(input('Digite o número: '))
cont = 0
for c in range(1, n + 1):
  if n % c == 0:
    cont += 1
print(f'O número {n} foi divisível {cont} vezes')
if cont <= 2:
  print('Por isso, ele é primo!')
else:
  print('Por isso, ele não é primo!')
  
