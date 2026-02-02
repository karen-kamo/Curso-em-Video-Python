'''enunciado: crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida'''
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2) / 2
if media < 5:
  print('REPROVADO')
elif media >= 5 and media <= 6.9:
  print('RECUPERAÇÃO')
else:
  print('APROVADO')