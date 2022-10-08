import speedtest
test = speedtest.Speedtest()

#faz teste de download e converte em mb/s
down = test.download()
rsDown = round(down)
fDown = int(rsDown / 1e+6)

#faz teste de upload e converte p mb/s
upload = test.upload()
rsUp = round(upload)
fUp = int(rsUp / 1e+6)

print(f'Velocidade de Download: {fDown} mb/s')
print(f'Velocidade de Upload: {fUp} mb/s')

sair = int(input("digite um número e aperte enter para sair!\n"))