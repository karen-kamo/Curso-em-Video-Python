import moeda
valor = float(input('Digite o preço: R$'))
print(moeda.aumentar(valor, 20))
print(moeda.diminuir(valor, 10))
print(moeda.dobro(valor))
print(moeda.metade(valor))
