palavras = (
    'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO'
)
for i in palavras:
    print(f'Na palavra {i} temos: ',end='')

    for letras in i:
        if letras in 'AEIOU':
            print(f'{letras} ', end='')
    print()