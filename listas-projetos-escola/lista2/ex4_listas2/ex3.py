lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for x in range(0, 3):
        lista[i][x] = int(input(f'Digite [{i}][{x}] número: '))

for i in range(0, 3):
    for x in range(0, 3):
        print(f'[{lista[i][x]}] ', end='')
    print()
    

