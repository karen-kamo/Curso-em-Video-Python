'''enunciado: faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: -quantidade de notas, - a maior nota, - a menor nota, - a média da turma, - a situação (opcional), adicione também as docstrings'''
def notas(* nts, situacao=False):
  '''Função que recebe um parâmetro múltiplo de notas, retornando um dicionário com as seguintes chaves:
  - Quantidade de notas
  - A maior nota
  - A menor nota
  - A média da turma
  - A situação (opcional)'''
  quant = soma = 0
  for pos, n in enumerate(nts):
    quant += 1
    soma += n
    if pos == 0:
      maior = n
      menor = n
    else:
      if n > maior:
        maior = n
      if n < menor:
        menor = n
  media = soma / quant
  d = {'quantidade': quant,
      'maior': maior,
      'menor': menor,
      'média': media}
  if situacao:
    if media >= 7:
      sit = 'BOM'
    elif 5 <= media < 7:
      sit = 'MEDIANA'
    else:
      sit = 'RUIM'
    d['situação'] = sit
  return d
print(notas(5.5, 2.5, 1.5, situacao=True))
help(notas)
quit