produtos = (
    'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
    'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90
)
print("-"*40)
print("          LISTAGEM DE PREÇOS")
print("-"*40)

for pro in range(0, len(produtos)):
    if pro % 2 == 0:
        x = len(produtos[pro])

        print(f'{produtos[pro]}', end='')
        print(f'.'*(30-x), end='')
        print("R$ ", end='')

    else:
        print(f'{produtos[pro]:.2f}')
print("-"*40)

#=======outro método============
print("\n\n", "="*30, "\n Outra forma de fazer:\n\n")

for pro in range(0, len(produtos)):
    if pro % 2 == 0:
        print(f'{produtos[pro]:.<30}', end='')
    else:
        print(f'R${produtos[pro]:>7.2f}')
print("-"*40)

#esquerda - '<'
#direita  - '>'
#centro   - '^'