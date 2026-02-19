'''enunciado: faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará'''
def ajuda(com):
  help(com)
#Programa principal
comando = '' 
while True:
  comando = str(input('Comando ou Biblioteca: '))
  if comando.upper() == 'FIM':
    print('Até a próxima!')
    break
  else:
    ajuda(comando)