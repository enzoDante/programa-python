
todos_cpfs_dados = list()
cpf_atributos = dict()

cpf_num = list()
cpf_num_copia = list()
multiplicar_cpf = list()
digitos_obtidos = list() #1º e 2º digito
valido_invalido = ''
result_multiplicar_cpf = 0
total_cpf = 0
cpfs_validos = 0
cpfs_invalidos = 0

while True:
    total_cpf += 1
    
    print('Digite seu CPF abaixo!')
    print('OBS: digite um número por vez, dando enter a cada digito do cpf!!!')
    for i in range(0, 11):
        num = int(input())
        while num < 0 or num > 9:
            num = int(input('Digite um digito de cada vez!!! entre 0 e 9!!! '))
        cpf_num.append(num)
    #gerando 1º digito do cpf----------------
    for i in range(10, 1, -1):
        multiplicar_cpf.append(i)
    for i in range(0, 9):
        result_multiplicar_cpf += cpf_num[i] * multiplicar_cpf[i]
    if result_multiplicar_cpf % 11 < 2:
        digitos_obtidos.append(0)
    else:
        digitos_obtidos.append(11 - (result_multiplicar_cpf % 11))
    #print(digitos_obtidos[0])
    #gerando 2º digito do cpf----------------
    
    cpf_num_copia = cpf_num[:]
    cpf_num_copia.pop()
    cpf_num_copia[9] = digitos_obtidos[0]
    multiplicar_cpf.insert(0, 11)
    result_multiplicar_cpf = 0
    for i in range(0, 10):
        result_multiplicar_cpf += cpf_num_copia[i] * multiplicar_cpf[i]
    
    if result_multiplicar_cpf % 11 < 2:
        digitos_obtidos.append(0)
    else:
        digitos_obtidos.append(11 - (result_multiplicar_cpf % 11))
    result_multiplicar_cpf = 0
    #analisar os dois últimos digitos obtidos com os dois últimos do cpf digitado
    if cpf_num[9] == digitos_obtidos[0] and cpf_num[10] == digitos_obtidos[1]:
        print('cpf válido!!!')
        valido_invalido = 'VÁLIDO'
        cpfs_validos += 1
    else:
        print('cpf inválido!!!')
        valido_invalido = 'INVÁLIDO'
        cpfs_invalidos += 1
    

    #limpando as listas principais!!!
    cpf_atributos['CPF'] = cpf_num[:]
    cpf_atributos['VALIDACAO'] = valido_invalido
    todos_cpfs_dados.append(cpf_atributos.copy())
    cpf_num.clear()
    digitos_obtidos.clear()
    multiplicar_cpf.clear()

    escolha = input('Você quer verificar mais cpfs? s/n\n')
    escolha = escolha.upper()
    while not escolha in 'SN':
        escolha = input('Você quer verificar mais cpfs? s/n\n').upper()

    if escolha == 'N':
        break
print(f'Total de CPFs testados: {total_cpf} ')
print(f'Total de CPFs válidos: {cpfs_validos} ')
print(f'Total de CPFs inválidos: {cpfs_invalidos} ')
print('Porcentagem de CPFs válidos: {:.1f}%'.format((cpfs_validos/total_cpf)*100))
print('Porcentagem de CPFs inválidos: {:.1f}%'.format((cpfs_invalidos/total_cpf)*100))
#essa parte abaixo não foi pedida no projeto, nn sei se precisa mostrar
for i in todos_cpfs_dados:
    print(f'{i}')