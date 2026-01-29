'''enunciado: faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''
nome = str(input('Digite o nome completo: ')).strip().title()
listaNome = nome.split()
print(f'O primeiro nome é: {listaNome[0]}')
print(f'O último nome é {listaNome[len(listaNome) - 1]}')
