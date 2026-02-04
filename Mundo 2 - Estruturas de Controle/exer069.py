'''enunciado: crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: a) quantas pessoas tem mais de 18 anos b)quantos homens foram cadastrados c) quantas mulheres tem menos de 20 anos'''
maiorIdade = quantH = quantM = 0
while True:
  idade = int(input('Digite a idade: '))
  sexo = ' '
  while sexo not in 'MF':
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
      maiorIdade += 1
    if sexo == 'M':
      quantH += 1
    else: 
      if idade <= 20:
        quantM += 1
  r = ' ' 
  while r not in 'SN':
    r = str(input('Quer adicionar mais pessoas? [S/N] ')).strip().upper()[0]
  if r == 'N':
    break
print(f'Tem {maiorIdade} pessoas com mais de 18 anos')
print(f'Foram cadastrados {quantH} homens')
print(f'Tem {quantM} mulheres com menos de 20 anos')