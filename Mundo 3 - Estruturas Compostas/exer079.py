'''enunciado: crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente'''
valores = []
r = 'S'
while r == 'S':
  valor = int(input('Digite um valor: '))
  if valor not in valores:
    valores.append(valor)
    print('Valor adicionado com sucesso...')
  else:
    print(f'{valor} já está inserido...')
  
  r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
valores.sort()
print(f'Você digitou os valores {valores}')


