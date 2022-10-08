lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
total = 0

for i in range(0, 3):
    for x in range(0, 3):
        lista[i][x] = int(input(f'Digite [{i}][{x}] número: '))
        total += lista[i][x]
for i in range(0, 3):
    for x in range(0, 3):
        if i == x:
            print(f'[{lista[i][x]}] ', end='')
        else:
            print('[ ] ', end='')
    print()