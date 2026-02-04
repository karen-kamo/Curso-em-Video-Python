'''enunciado: crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''
n = int(input('Digite o número: '))
soma = n
cont = 1
while n != 999:
  n = int(input('Digite o número: '))
  if n != 999:
    cont += 1
    soma += n
print(f'A soma dos {cont} números é {soma}')