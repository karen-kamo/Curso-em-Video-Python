'''enunciado: desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo'''
r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
  print('Podem formar um triângulo')
else:
  print('Não podem formar um triângulo.')