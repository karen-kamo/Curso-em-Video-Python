'''enunciado: faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''
for c in range(1, 6):
  peso = float(input(f'Digite o peso da pessoa {c}: '))
  if c == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    elif peso < menor:
      menor = peso
print(f'Maior: {maior:.2f}. Menor: {menor:.2f}')