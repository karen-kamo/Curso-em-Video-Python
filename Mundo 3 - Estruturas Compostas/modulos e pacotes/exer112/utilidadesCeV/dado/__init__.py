'''enunciado: dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma funçao chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários'''

def leiaDinheiro(msg):
  valido = False
  while not valido:
    entrada = str(input(msg)).replace(',', '.').strip()
    if entrada.isalpha() or entrada == '':
      print(f'ERRO: \"{entrada}\" é um preço inválido!')
    else:
      valido = True
      return float(entrada)