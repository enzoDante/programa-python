time = dict()
gols = list()

nome = input('Digite o nome de um time: ')
partidas = int(input('Partidas disputadas: '))

total = 0
for i in range(partidas):
    gol = int(input(f'Quantos gols fizeram na {i+1}º partida: '))
    gols.append(gol)
    total += gol

time['nome'] = nome
time['partidas'] = partidas
time['gol_partida'] = gols
time['total_gols'] = total

for p, v in enumerate(time['gol_partida']):
    print(f'  Partida {p+1} : {v} gols ')
print(f'Total de gols ===> {time["total_gols"]}')