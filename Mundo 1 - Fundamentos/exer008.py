'''enunciado: escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
n = int(input('Digite um valor em metros: '))
cm = n * 100
mm = n * 1000
print(f'{n} metros equivale a {cm} cm e a {mm} mm')