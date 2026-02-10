'''enunciado: crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta'''
e = str(input('Digite a expressão: ')).strip()
pilha = []
for simb in e:
  if simb == '(':
    pilha.append('(')
  elif simb == (')'):
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
      break
if len(pilha) == 0:
  print('É uma expressão válida!')
else:
  print('Não é uma expressão válida!')
