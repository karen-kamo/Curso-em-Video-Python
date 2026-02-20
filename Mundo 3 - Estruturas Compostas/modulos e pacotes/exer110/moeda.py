'''enunciado: adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algbumas informações geradas pelas funções que já temos no módulo criado até aqui'''
def moeda(n = 0, moeda = 'R$'):
  return f'{moeda}{n:>.2f}'.replace('.', ',')

def aumentar(n = 0, taxa = 0, formatar=False):
  aum = n * taxa / 100
  res = n + aum
  return res if formatar is False else moeda(res)

def diminuir(n = 0, taxa = 0, formatar=False):
  dim = n * taxa / 100
  res = n - dim
  return res if formatar is False else moeda(res)

def dobro(n = 0, formatar=False):
  res = n * 2
  return res if formatar is False else moeda(res)

def metade(n = 0, formatar=False):
  res = n / 2
  return res if formatar is False else moeda(res)

def resumo(v = 0, aum = 0, dim = 0):
  print('-' * 30)
  print('RESUMO DO VALOR'.center(30))
  print('-' * 30)
  print(f'Preço analisado: \t{moeda(v)}')
  print(f'Dobro do preço: \t{dobro(v, True)}')
  print(f'Metade do preço: \t{metade(v, True)}')
  print(f'{aum}% de aumento: \t{aumentar(v, aum, True)}')
  print(f'{dim}% de redução: \t{diminuir(v, dim, True)}')
