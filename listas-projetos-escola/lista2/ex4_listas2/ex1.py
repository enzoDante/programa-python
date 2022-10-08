from functools import total_ordering


lista = list()
dados = list()
i = 0
menor_salario = 0
while True:
    i += 1
    dados.append(input(f'Digite {i}º nome: '))
    dados.append(float(input('Digite o salário: ')))

    if i == 1:
        menor_salario = dados[1]

    elif dados[1] < menor_salario:
        menor_salario = dados[1]

    lista.append(dados[:])
    dados.clear()

    continuar = input('Inserir mais pessoas? s/n\n')
    continuar = continuar.upper()
    while not continuar == "S" and not continuar == "N":
        continuar = input('digite--> s/n\n')
        continuar = continuar.upper()
    if continuar == 'N':
        break

total_salario = 0
total_pessoas = i

for salario in lista:
    total_salario += salario[1]
    print(f'salario = [{salario[1]:.2f}]')
print(f'\nTotal = [{total_salario:.2f}]')
print(f'[{total_pessoas}] pessoas informadas')
print(f'Menor salário = [{menor_salario:.2f}]')



"""for i, valores in enumerate(lista):
    total_salario += valores[1]
    print(f'salario = {valores[1]:.2f} ')
print(total_salario)"""


"""for nome, salario in lista:
    total_salario += salario
    """
