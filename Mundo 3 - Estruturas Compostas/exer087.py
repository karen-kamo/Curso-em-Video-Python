'''enunciado: aprimore o desafio anterior, mostrando no final: a) a soma de todos os valores pares digitados b) a soma dos valores da terceira coluna c) o maior valor da segunda linha'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = sTerCol = maior = 0
for l in range(0, 3):
  for c in range(0, 3):
    n = int(input(f'Valor do [{l}][{c}]: '))
    matriz[l][c] = n
    if n % 2 == 0:
      soma += n
    if c == 2:
      sTerCol += n
    if l == 1:
      if c == 0:
        maior = n
      else:
        if n > maior:
          maior = n
for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{matriz[l][c]}]', end='')
  print()
print(f'Soma dos pares: {soma}')
print(f'Soma da terceira coluna: {sTerCol}')
print(f'Maior da segunda linha: {maior}')