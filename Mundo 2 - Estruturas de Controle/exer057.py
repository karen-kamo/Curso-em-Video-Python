'''enunciado: faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto'''
sexo = str(input('Digite o sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
  print('Entrada inválida!')
  sexo = str(input('Digite o sexo: ')).strip().upper()[0]
if sexo == 'M':
  print('Sexo Masculino registrado!')
elif sexo == 'F':
  print('Sexo Feminino registrado!')