from random import randint

lista = list()
total_de_jogos = list()

jogos = int(input('Quantos jogos da mega senha deve ser gerados? '))
while jogos < 1:
    jogos = int(input('Quantos jogos? '))

for x in range(jogos):
    numeros_ficha = 0
    while True:
        num = randint(1, 60)
        while num in lista:
            num = randint(1, 60)
        lista.append(num)

        numeros_ficha += 1
        if numeros_ficha >= 6:
            break
    total_de_jogos.append(lista[:])
    lista.clear()

for valores in total_de_jogos:
    print(valores)
