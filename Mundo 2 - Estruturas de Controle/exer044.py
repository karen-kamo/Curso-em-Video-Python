'''enunciado: elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento'''
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro
[2] à vista cartão
[3] 2x cartão
[4] 3x ou mais cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
  desconto = (preco * 10) / 100
  print(f'O preço final será de R${preco - desconto}')
elif opcao == 2:
  desconto = (preco * 5) / 100
  print(f'O preço será de R${preco - desconto}')
elif opcao == 3:
  print(f'O valor da parcela em 2x será de R${preco / 2:.2f}')
elif opcao == 4:
  juros = (preco * 20) / 100
  parcelas = int(input('Quantas parcelas? '))
  print(f'Sua compra será parcelada em 10x de R${preco + juros:.2f} com JUROS')
  print(f'O preço com o juros será de R${preco + juros}')
