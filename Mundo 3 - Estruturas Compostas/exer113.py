'''enunciado: reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade'''
def leiaInt(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print('ERRO: digite um número inteiro válido!')
      continue
    except (KeyboardInterrupt):
      print('\nEntrada de dados interrompida pelo usuário!')
      return 0
    else:
      return n
    
def leiaFloat(msg):
  while True:
    try:
      n = float(input(msg))
    except (ValueError, TypeError):
      print('ERRO: digite um número válido!')
      continue
    except (KeyboardInterrupt):
      print('\nEntrada de dados interrompida pelo usuário!')
      return 0
    else:
      return n
num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')
f = leiaFloat('Digite um valor flutuando: ')
print(f'O valor digitado foi {f:.1f}')