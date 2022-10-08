def verificarmedia(nota):
    '''
    verifica a nota de um aluno e retorna uma mensagem de acordo com o valor passado no parametro
    :param nota:
    '''
    if nota >= 6:
        msg = "Aluno Aprovado!"
    elif nota >= 3.5 and nota < 6:
        msg = "Aluno em exame!"
    else:
        msg = "Aluno reprovado!"
    return msg
    
#help(verificarmedia)
while True:
    media = float(input('Digite a nota final do Aluno: '))
    while media < 0 or media > 10:
        media = float(input('Digite corretamente a nota final do Aluno: '))
    print(verificarmedia(media))

    if int(input('deseja continuar? 1-sim/qualquer número-não\n')) != 1:
        break