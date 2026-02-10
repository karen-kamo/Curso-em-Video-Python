'''enunciado: crie um programa que vai ler vários números e colocar uma lista. Depois disso, mostre: a) quantos números foram digitados b) a lista de valores, ordenada de forma decrescente c) se o valor 5 foi digitado e está ou não na lista'''
lista = []
while True:
  n = int(input('Digite um número: '))
  lista.append(n)
  r = str(input('Deseja adicionar mais? [S/N] ')).strip().upper()[0]
  if r in 'Nn':
    break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Lista decrescente: {lista}')
esta = False
for num in lista:
  if num == 5:
    esta = True 
if esta:
    print('O número 5 está na lista.')
else:
  print('O número 5 não está na lista')