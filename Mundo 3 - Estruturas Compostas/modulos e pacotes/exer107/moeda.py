'''enunciado: crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''
def aumentar(n):
  aum = n * 10 / 100
  return f'Aumentando 10%, temos R${n + aum:.1f}'

def diminuir(n):
  dim = n * 10 / 100
  return f'Diminuindo 10%, temos R${n - dim:.1f}'

def dobro(n):
  return f'O dobro de R${n:.1f} é R${n*2:.1f}'

def metade(n):
  return f'A metade de R${n:.1f} é R${n/2:.1f}'