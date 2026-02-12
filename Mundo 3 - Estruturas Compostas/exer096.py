'''enunciado: faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno'''
def area(l, c):
  return l * c
largura = float(input('Digite a largura: '))
comp = float(input('Digite o comprimento: '))
print(f'Área do terreno é: {area(largura, comp):.1f}m²')