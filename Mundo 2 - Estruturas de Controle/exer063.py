'''enunciado: escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci'''
n = int(input('Quantos termos você quer ver? '))
proximo = 0
anterior = cont = 1
while cont <= n:
  print(f'{proximo} -', end=' ')
  temp = proximo
  proximo = proximo + anterior
  anterior = temp
  cont += 1
print('FIM')