'''enunciado: escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.'''
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário: R$'))
anos = int(input('Digite em quantos anos irá pagar: '))
prestacao = casa / (anos * 12)
valor = salario * 30 / 100
print(f'O valor da prestação é de R${prestacao:.2f}')
if prestacao >= valor:
  print('O empréstimo será negado.')
else:
  print('O empréstimo foi aceito!')