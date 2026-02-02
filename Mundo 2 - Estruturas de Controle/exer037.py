'''enunciado: escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.'''
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Digite a opção: '))
if opcao == 1:
  print(f'{n} convertido para binário é {bin(n)[2:]}')
elif opcao == 2:
  print(f'{n} convertido para octal é {oct(n)[2:]}')
elif opcao == 3:
  print(f'{n} convertido para hexadecimal é {hex(n)[2:]}')
else:
  print('Digite uma opção válida!')