'''enunciado: faça um programa que leia um ano qualquer e mostre se ele é bissexto'''
ano = int(input('Digite um ano: '))
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
  print(f'O ano {ano} é bissexto!')
else:
  print('Não é bissexto.')