'''enunciado: faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
preco = float(input('Digite o preço: '))
desconto = (preco * 5) / 100
print(f'O novo preço do produto é R${preco - desconto:.2f}')