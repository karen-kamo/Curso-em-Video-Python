'''enunciado: faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada'''
def contador(inicio, fim , passo):
  if passo < 0:
    passo *= -1
  if passo == 0:
    passo = 1
  print('=' * 30)
  print(f'Contador de {inicio} até {fim}, de {passo} em {passo}')
  if inicio < fim:
    for c in range(inicio, fim + 1, passo):
      print(f'{c} - ', end='')
    print('Fim')
  else:
    cont = inicio
    while cont >= fim:
      print(f'{cont} - ', end='')
      cont -= passo
    print('Fim')
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)