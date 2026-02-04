'''enunciado: faça um programa que leia um número qualquer e mostre o seu fatorial'''
n = int(input('Digite o número: '))
f = 1
while n != 1:
  f *= n
  n -= 1
print(f'O fatorial é {f}')