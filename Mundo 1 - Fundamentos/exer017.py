'''enunciado: faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''
import math
catOposto = float(input('Digite o cateto oposto: '))
catAdj = float(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(catOposto, catAdj)
print(f'A hipotenusa vale {hipotenusa}')