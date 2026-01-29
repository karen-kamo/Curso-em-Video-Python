'''enunciado: crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar.
considere US$1,00 = R$3,27'''

valor = float(input('Digite a quantidade de dinheiro da carteira: '))
dolar = valor / 3.27
print(f'O valor de R${valor} equivale a US${dolar:.2f}')