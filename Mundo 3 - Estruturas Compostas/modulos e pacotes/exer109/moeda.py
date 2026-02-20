'''enunciado: modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108'''
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

