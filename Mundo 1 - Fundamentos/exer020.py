'''enunciado: o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
import random
n1 = str(input('Digite o aluno 1: '))
n2 = str(input('Digite o aluno 2: '))
n3 = str(input('Digite o aluno 3: '))
n4 = str(input('Digite o aluno 4: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem decidida foi: {lista}')
