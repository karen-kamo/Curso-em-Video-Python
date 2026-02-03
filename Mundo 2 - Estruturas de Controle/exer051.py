'''enunciado: desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa prograssão'''
pTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
dTermo = pTermo + (10 - 1) * razao
for c in range(pTermo, dTermo + razao, razao):
  print(f'{c} -', end=' ')
print('Acabou', end=' ')