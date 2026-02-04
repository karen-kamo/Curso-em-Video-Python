'''enunciado: crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores'''
r = 'S'
cont = soma = 0
while r != 'N':
  n = int(input('Digite o número: '))
  cont += 1
  soma += n
  if cont == 1:
    maior = menor = n
  else:
    if n > maior:
      maior = n
    elif n < menor:
      menor = n
  r = str(input('Quer continuar? ')).strip().upper()[0]
print(f'A média é {soma / cont:.2f}. O maior é {maior} e o menor é {menor}')