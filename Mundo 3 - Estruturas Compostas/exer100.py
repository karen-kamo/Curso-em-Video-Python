'''enunciado: faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior'''
from random import randint

numeros = []
def sorteia(lista):
  for c in range(5):
    n = randint(0, 10)
    lista.append(n)

def somaPar(lista):
  soma = 0
  for n in lista:
    if n % 2 == 0:
      soma += n
  return soma

sorteia(numeros)
print(f'Lista: {numeros}')
print(f'Soma: {somaPar(numeros)}')