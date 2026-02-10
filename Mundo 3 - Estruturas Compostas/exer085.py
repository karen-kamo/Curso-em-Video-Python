'''enunciado: crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crsecente'''
lista = [[], []]
for c in range(0, 7):
  n = int(input('Digite o número: '))
  if n % 2 == 0:
    lista[0].append(n)
  else:
    lista[1].append(n)
lista[0].sort()
print(f'Pares: {lista[0]}')
lista[1].sort()
print(f'Ímpares: {lista[1]}')