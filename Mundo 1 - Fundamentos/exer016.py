'''enunciado: crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.'''
import math
n = float(input('Digite um número: '))
print(f'O valor digitado foi {n} e sua porção inteira é {math.trunc(n)}')