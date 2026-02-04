'''enunciado: crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues'''
valor = int(input('Digite o valor a ser sacado: R$'))
quant100 = quant50 = quant20 = quant10 = quant5 = quant2 = quant1 = 0
while True:
  if valor >= 100:
    quant100 += 1
    valor -= 100
  else:
    if valor >= 50:
      quant50 += 1
      valor -= 50
    else:
      if valor >= 20:
        quant20 += 1
        valor -= 20
      else:
        if valor >= 10:
          quant10 += 1
          valor -= 10
        else:
          if valor >= 5:
            quant5 += 1
            valor -= 5
          else:
            if valor >= 2:
              quant2 += 1
              valor -= 2
            else:
              if valor >= 1:
                quant1 += 1
                valor -= 1
  if valor <= 0:
    break
print(f'Cédulas de R$100: {quant100}')
print(f'Cédulas de R$50: {quant50}')
print(f'Cédulas de R$20: {quant20}')
print(f'Cédulas de R$10: {quant10}')
print(f'Cédulas de R$5: {quant5}')
print(f'Cédulas de R$2: {quant2}')
print(f'Cédulas de R$1: {quant1}')
