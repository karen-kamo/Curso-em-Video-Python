'''enunciado: faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²'''
largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))
area = largura * altura
latas = area / 2
print(f'Com a largura de {largura}m e altura de {altura}m pode-se pintar uma área de {area}m² com {latas}l de tinta.')