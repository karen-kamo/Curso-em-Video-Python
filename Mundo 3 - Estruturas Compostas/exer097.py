'''enunciado: faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável'''
def escreva(msg):
  tam = 4 + len(msg)
  print('~' * tam)
  print(f'  {msg}')
  print('~' * tam)
frase = str(input('Digite a frase: ')).strip()
escreva(frase)