'''enunciado: faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''
salario = float(input('Digite o salário: '))
novo = salario + ((salario * 15) / 100)
print(f'O novo salário do funcionário é de R${novo:.2f}')
