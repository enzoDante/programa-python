
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
    print('='*62)
    print('Digite seu CPF abaixo!')
    print('OBS: todos os digitos juntos sem (.) ou (-) !!!')
    print('='*62)
    
    num = str(input())
    while not len(num) == 11 or num.count('.') > 0 or num.count('-') > 0 or num.count(' ') > 0:
        num = str(input('Digite todos os 11 dígitos corretamente, evite usar "." ou "-"!!!\n'))
    for i in range(0, 11):
        cpf_num.append(int(num[i]))
    #gerando 1º digito do cpf----------------
    c_multip = 10
    for i in range(0, 9):
        multiplicar_cpf.append(c_multip)
        c_multip -= 1
        result_multiplicar_cpf += cpf_num[i] * multiplicar_cpf[i]
    if result_multiplicar_cpf % 11 < 2:
        digitos_obtidos.append(0)
    else:
        digitos_obtidos.append(11 - (result_multiplicar_cpf % 11))
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
        print('='*62)
        print('cpf válido!!!')
        valido_invalido = 'VÁLIDO'
        cpfs_validos += 1
    else:
        print('='*62)
        print('cpf inválido!!!')
        valido_invalido = 'INVÁLIDO'
        cpfs_invalidos += 1
    print(digitos_obtidos)
    print('='*62)

    #atribuindo valores importantes!!!
    cpf_atributos['CPF'] = num
    cpf_atributos['VALIDACAO'] = valido_invalido
    todos_cpfs_dados.append(cpf_atributos.copy())
    #limpando as listas principais!!!
    cpf_num.clear()
    digitos_obtidos.clear()
    multiplicar_cpf.clear()

    escolha = input('Você quer verificar mais cpfs? s/n\n')
    escolha = escolha.upper()
    while not escolha in 'SN':
        print('-'*62)
        escolha = input('Você quer verificar mais cpfs? s/n\n').upper()

    if escolha == 'N':
        break
print('='*62)
print(f'Total de CPFs testados: {total_cpf} ')
print(f'Total de CPFs válidos: {cpfs_validos} ')
print(f'Total de CPFs inválidos: {cpfs_invalidos} ')
print('Porcentagem de CPFs válidos: {:.1f}%'.format((cpfs_validos/total_cpf)*100))
print('Porcentagem de CPFs inválidos: {:.1f}%'.format((cpfs_invalidos/total_cpf)*100))
print('='*62)
#essa parte abaixo não foi pedida no projeto, nn sei se precisa mostrar
for i in todos_cpfs_dados:
    print(f'{i}')