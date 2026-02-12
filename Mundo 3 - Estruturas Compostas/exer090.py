'''enunciado: faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela'''
aluno = dict()
aluno['nome'] = str(input('Digite o nome: ')).strip().title()
aluno['media'] = float(input('Digite  a média: '))
if aluno['media'] >= 7:
  aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
  aluno['situação'] = 'Recuperação'
else:
  aluno['situação'] = 'Reprovado'
print('-=' * 30)
print(f'- nome é a {aluno["nome"]}')
print(f'- média é igual a {aluno["media"]:.1f}')
print(f'- situação é igual a {aluno["situação"]}')
