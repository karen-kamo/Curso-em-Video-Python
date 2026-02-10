'''enunciado: crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
pares = []
impares = []
while True:
  n = int(input('Digite o valor: '))
  lista.append(n)
  if n % 2 == 0:
    pares.append(n)
  else:
    impares.append(n)
  r = str(input('Quer adicionar mais? [S/N] ')).strip().upper()[0]
  if r in 'N':
    break
print(f'Lista toda {lista}')
print(f'Lista dos pares {pares}')
print(f'Lista dos ímpares {impares}')