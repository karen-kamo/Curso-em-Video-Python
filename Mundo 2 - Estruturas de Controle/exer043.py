'''enunciado: desenvolva uma lógoica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo'''

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura * altura)
print(f'IMC: {imc:.2f}')
if imc < 18.5:
  print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
  print('Peso ideal')
elif imc >= 25 and imc < 30:
  print('Sobrepeso')
elif imc >= 30 and imc < 40:
  print('Obesidade')
else:
  print('Obesidade mórbida')