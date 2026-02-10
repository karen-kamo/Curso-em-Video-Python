'''enunciado: faça um programa que leia os 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista'''
lista = []
maior = menor = posMaior = posMenor = 0
for c in range(1, 6):
  n = float(input(f'Digite o {c}º número: '))
  lista.append(n)
for pos, n in enumerate(lista):
  if pos == 0:
    maior = menor = n
  else:
    if n > maior:
      maior = n
      posMaior = pos
    elif n < menor:
      menor = n
      posMenor = pos
print(f'Lista: {lista}')
print(f'O maior número {maior} está na posição {posMaior}ª')
print(f'O menor número {menor} está na posição {posMenor}ª')
