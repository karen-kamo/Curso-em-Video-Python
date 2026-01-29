'''enunciado: faça um programa que leia uma frase pelo teclado e mostre: - quantas vezes aparece a letra A, - em que posição ela aparece a primeira vez, - em que posição aparece a última vez'''
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'O A aparece {frase.count('A')} vezes.')
print(f'A primeira vez que aparece é no índice: {frase.find('A')}')
print(f'A última vez que aparece é no índice: {frase.rfind('A')}')
