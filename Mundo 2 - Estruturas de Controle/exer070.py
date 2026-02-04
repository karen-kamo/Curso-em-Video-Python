'''enunciado: crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: a)qual é o total gasto na compra b) quantos produtos custam mais de R$1000 c) qual é o nome do produto mais barato'''
soma = caros = cont = pBarato = 0
nBarato = ' '
while True:
  produto = str(input('Nome do produto: ')).strip()
  preco = float(input('Preço: R$'))
  soma += preco
  if preco > 1000:
    caros += 1
  if cont == 0:
    pBarato = preco
    nBarato = produto
  else:
    if preco < pBarato:
      pBarato = preco
      nBarato = produto
  cont += 1
  r = ' '
  while r not in 'SN':
    r = str(input('Quer adicionar mais produto? [S/N] ')).strip().upper()[0]
  if r == 'N':
    break
  print('-' * 30)
print(f'O total gasto foi R${soma:.2f}')
print(f'{caros} produtos custam mais de R$1000')
print(f'{nBarato.title()} é o produto mais barato, sendo R${pBarato}')
