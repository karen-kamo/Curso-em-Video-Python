'''enunciado: melhore o desafio 0 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos'''
pTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = pTermo
cont = 1
while cont <= 10:
  print(f'{termo} -', end=' ')
  termo += razao
  cont += 1
print('PAUSA')

quant = int(input('Quantos termos você quer mostrar a mais? '))
while quant != 0:
  cont = 1
  while cont <= quant:
    print(f'{termo} -', end=' ')
    termo += razao
    cont += 1
  print('PAUSA')
  quant = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')