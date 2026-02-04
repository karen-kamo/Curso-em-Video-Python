'''enunciado: crie um programa que leia dois valores e mostre um menu como o ao lado na tela:'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
  print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
  opcao = int(input('Digite a sua opção: '))
  if opcao == 1:
    print(f'A soma entre {n1} e {n2} é {n1 + n2}')
  elif opcao == 2:
    print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
  elif opcao == 3:
    if n1 > n2:
      print(f'{n1} é maior que {n2}')
    else:
      print(f'{n2} é maior que {n2}')
  elif opcao == 4:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('Os novos números foram registrados!')
  else:
    print('Digite uma opção válida!')
print('Fim do programa!')