'''enunciado: crie um programa que leia o nome completo de uma pessoa e mostre: - o nome com todas as letras maiúsculas, - o nome com todas as minúsculas, - quantas letras ao todos (sem considerar os espaços), - quantas letras tem o primeiro nome'''
nome = str(input('Digite o seu nome completo: ')).strip()
print(f'O nome em maiúsculo é {nome.upper()}')
print(f'O nome em minúsculo é {nome.lower()}')

listaNome = nome.split()
nomeSem = ''.join(listaNome)
print(f'A quantidade de letras é {len(nomeSem)}')

primeiroNome = listaNome[0]
print(f'A quantidade de letras do primeiro nome é {len(primeiroNome)}')