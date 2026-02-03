'''enunciado: desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: - A média de idade do grupo, - Qual é o nome do homem mais velho, - Quantas mulheres têm menos de 20 anos'''
soma = 0
idVelho = 0
hVelho = ''
fNovas = 0
for c in range(1, 5):
  nome = str(input('Nome: ')).strip().title()
  idade = int(input('Idade: '))
  sexo = str(input('Sexo(M ou F): ')).strip().upper()

  soma += idade

  if sexo == 'M':
    if idVelho == 0:
      idVelho = idade
      hVelho = nome
    else:
      if idade > idVelho:
        idVelho = idade
        hVelho = nome
  elif sexo == 'F':
    if idade <= 20:
      fNovas += 1
  
print(f'Média: {soma / 4:.2f}')
print(f'Homem mais velho: {hVelho} com {idVelho} anos')
print(f'Tem {fNovas} mulheres com menos de 20 anos')