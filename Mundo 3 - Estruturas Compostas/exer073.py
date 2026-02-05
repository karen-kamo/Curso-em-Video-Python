'''enunciado: crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) os 5 primeiros b) os últimos 4 colocados c) times em ordem alfabética d) em que posição está o time da Chapecoense'''
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os últimos colocados são: {times[16:20]}')
print(f'Ordem: alfabética: {sorted(times)}')
print(f'Chapecoense está na posição {times.index('Chapecoense')+1}ª')
