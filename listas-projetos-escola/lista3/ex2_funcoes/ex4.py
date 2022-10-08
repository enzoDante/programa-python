
def digitenumero(msg):
    '''
    sera passado como parametro uma mensagem para ser mostrada ao usuario, e nessa mesma mensagem o usuario ira digitar um numero inteiro que tambem sera retornado
    '''
    num = int(input(msg))
    return num

#help(digitenumero)
n = digitenumero("Digite um numero: ")
print(f'O número inteiro digitado foi {n}')