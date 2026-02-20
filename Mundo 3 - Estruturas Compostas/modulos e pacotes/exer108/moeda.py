'''enunciado: adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado'''
def moeda(n = 0, moeda = 'R$'):
  return f'{moeda}{n:.1f}'

def aumentar(n = 0, taxa = 0):
  aum = n * taxa / 100
  res = n + aum
  return f'Aumentando {taxa}%, temos {moeda(res)}'

def diminuir(n = 0, taxa = 0):
  dim = n * taxa / 100
  res = n - dim
  return f'Diminuindo {taxa}%, temos {moeda(res)}'

def dobro(n = 0):
  return f'O dobro de {moeda(n)} é {moeda(n * 2)}'

def metade(n = 0):
  return f'A metade de {moeda(n)} é {moeda(n / 2)}'

