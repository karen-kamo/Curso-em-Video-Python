'''enunciado: crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero a vinte. Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso'''
nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', ' dezoito', 'dezenove', 'vinte')
while True:
  esc = int(input('Digite um número entre 0 e 20: '))
  if 0 <= esc <= 20:
    break
for pos, n in enumerate(nums):
  if pos + 1 == esc:
    print(nums[pos+1].title())
  
  
