def Valida_CPF(cpf_num):
    '''
    :param cpf_num: lista, todos os numeros do cpf estarao aqui exemp[1,2,3,4,5,6,7,8,9,1,0]
    :return: retornara 'CPF valido' ou 'CPF invalido' apos analisar o cpf informado
    '''

    #cpf_num = list()---------------------
    cpf_num_copia = list()
    multiplicar_cpf = list()
    digitos_obtidos = list() #1º e 2º digito
    valido_invalido = ''
    result_multiplicar_cpf = 0

    #for i in range(0, 11):--------------------------------
        #cpf_num.append(int(cpf[i]))-----------------------
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
        valido_invalido = 'CPF VÁLIDO'
    else:
        valido_invalido = 'CPF INVÁLIDO'
    
    #limpando as listas principais!!!
    #cpf_num.clear()
    digitos_obtidos.clear()
    multiplicar_cpf.clear()

    return valido_invalido

