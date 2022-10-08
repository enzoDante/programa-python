def verificar_idade(val):    
    '''
    nome e idade sao opcionais, os valores informados serao adicionados em uma lista e essa lista sera passada como parametro, as variaveis 'informa_nome' e 'informa_idade' receberao True ou False 

    exemp(informa_idade = True): se for verdadeiro, significa que a idade foi informada, entao sera verificado se eh ou nao maior de idade
    exemp(informa_nome = True): usuario informou um nome, ira mostrar o nome
    '''
    print('=-' * 30)
    msg = ''
    if informa_nome:
        msg += f'Nome informado: {val[0]}\n'
    else:
        msg += 'Nome não informado\n'
    if informa_idade and informa_nome:
        if val[1] >= 18:
            msg += 'Você é maior de idade'
        else:
            msg += 'Você é menor de idade'
    elif informa_idade and informa_nome == False:
        if val[0] >= 18:
            msg += 'Você é maior de idade'
        else:
            msg += 'Você é menor de idade'
    else:
        msg += 'Idade não informado'
    return msg

#help(verificar_idade)
valores = list()
informa_nome = False
informa_idade = False

if input('Deseja informar seu nome? s:').upper() == 'S':
    nome = input('Digite seu nome: ')
    informa_nome = True
    valores.append(nome)

if input('Deseja informar sua idade? s:').upper() == 'S':
    idade = int(input('Digite sua idade: '))
    while idade <= 0:
        idade = int(input('Digite sua idade corretamente: '))
    informa_idade = True
    valores.append(idade)

print(verificar_idade(valores))