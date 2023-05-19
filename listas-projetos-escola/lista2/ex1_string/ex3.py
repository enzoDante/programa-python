cidade = input('Digite o nome de uma cidade:   ')
cidade = cidade.split()
print(cidade)

print(f'\n\n{cidade[0].find("São")}')
if cidade[0].find('São') < 0 or cidade[0].find('São') >= 1:
    print('Não começa com a palavra [São]')
else:
    print('Começa com a palavra [São]')

print(f"teste {cidade[0].find('sao')}")
print(f"aa {cidade[0][2:5]}")