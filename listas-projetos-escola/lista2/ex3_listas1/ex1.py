lista = list()
maior = menor = 0
for x in range(0, 5):
    num = int(input(f"Digite {x+1}º número:  "))
    lista.append(num)
for i, v in enumerate(lista):
    if i == 0:
        maior = menor = v

    elif v > maior:
        maior = v

    elif v < menor:
        menor = v
print(f'O maior número foi: [{maior}] na(s) posição(ões): ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1} ',end='')

print(f'\nMenor número foi [{menor}] na(s) posição(ões): ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1} ', end='')

print('\n\n')
print(lista)