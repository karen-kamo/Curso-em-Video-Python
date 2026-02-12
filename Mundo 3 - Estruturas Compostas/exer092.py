'''enunciado: crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule a acrescente, além da idade, com quantos anos a pessoa vai se aposentar'''
from datetime import date
trab = dict()
trab['nome'] = str(input('Digite o nome: ')).strip().title()
nasc = int(input('Digite o ano de nascimento: '))
atual = date.today().year
trab['idade'] = atual - nasc
print(trab)
trab['ctps'] = int(input('Digite o CTPS (0 se não tem): '))
if trab['ctps'] != 0:
  trab['contratação'] = int(input('Digite o ano de contratação: '))
  trab['salário'] = float(input('Digite o salário: R$'))
  trab['aposentadoria'] = trab['idade'] + ((trab['contratação'] + 35) - atual)
print('-=' * 30)
for k, v in trab.items():
  print(f' - {k} tem o valor {v}')