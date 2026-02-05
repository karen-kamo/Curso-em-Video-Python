'''enunciado: desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: a) quantas vezes apareceu o valor 9 b) em que posição foi digitado o primeiro valor 3 c) quais foram os números pares'''
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
n4 = int(input('Digite o 4º número: '))
nums = (n1, n2, n3, n4)
quant9 = quantPares = 0 
for n in nums:
  if n == 9:
    quant9 += 1
  if n % 2 == 0:
    quantPares += 1
print(f'O 9 apareceu {quant9} vezes')
print(f'Posição que aparece 3 pela primeira vez: {nums.index(3)}')
print(f'Quantidade de números pares: {quantPares}')