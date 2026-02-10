'''enunciado: faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: a) quantas pessoas foram cadastradas b) uma listagem com as pessoas mais pesadas c) uma listagem com as pessoas mais leves'''
pessoas = []
pessoasPesadas = []
pessoasLeves = []
maisPesado = maisLeve = cont = 0
while True:
  nome = str(input('Digite o nome: ')).strip().title()
  peso = float(input('Digite o peso: '))
  if cont == 0:
    maisPesado = peso
    maisLeve = peso
  else:
    if peso > maisPesado:
      maisPesado = peso
    elif peso < maisLeve:
      maisLeve = peso
  pessoa = [nome, peso]
  pessoas.append(pessoa)
  cont += 1
  r = str(input('Quer adicionar mais? [S/N] ')).strip().upper()[0]
  if r in 'N':
    break
for pos, pessoa in enumerate(pessoas):
  if maisPesado in pessoa:
    pessoasPesadas.append(pessoa[0])
  if maisLeve in pessoa:
    pessoasLeves.append(pessoa[0])
print(f'Ao todos, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maisPesado:.1f}Kg. Peso de {pessoasPesadas}')
print(f'O menor peso foi de {maisLeve:.1f}Kg. Peso de {pessoasLeves}')
