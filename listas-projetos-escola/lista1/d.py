tempo = float(input("Digite o tempo gasto da viagem:\n"))
velo = float(input("Digite a velocidade média:\n"))

dist = tempo * velo
litros = dist/12

print(f'velocidade = {velo} tempo = {tempo} distancia = {dist} litros gastos = {litros:.2f}')
