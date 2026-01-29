'''enunciado: crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome'''
nome = str(input('Digite o nome: ')).strip().upper()
print(f'Seu nome tem SILVA? {'SILVA' in nome}')