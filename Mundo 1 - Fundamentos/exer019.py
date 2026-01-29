'''enunciado: um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'''
import random
n1 = str(input('Digite o aluno 1: '))
n2 = str(input('Digite o aluno 2: '))
n3 = str(input('Digite o aluno 3: '))
n4 = str(input('Digite o aluno 4: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O escolhido foi o {escolhido}')