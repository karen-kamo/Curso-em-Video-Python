'''enunciado: crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente'''
lista = []
while True:
  nome = str(input('Digite o nome: ')).strip().title()
  n1 = float(input('Digite a nota 1: '))
  n2 = float(input('Digite a nota 2: '))
  media = (n1 + n2) / 2
  aluno = [nome, [n1, n2], media]
  lista.append(aluno)
  r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if r == 'N':
    break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)
for i, a in enumerate(lista):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
  print('-' * 35)
  esc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
  if esc == 999:
    print('Volte sempre!')
    break
  if esc <= len(lista) - 1:
    print(f'Notas de {lista[esc][0]} são {lista[esc][1]}')
