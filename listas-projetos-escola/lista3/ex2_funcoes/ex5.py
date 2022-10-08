def analise_faturamento(val):
    '''
    passara como parametro uma lista com todas as faturas, ira retornar o total de faturas, maior e menor valor das faturas e a media de todas as faturas informadas
    '''
    maior = menor = 0
    total = 0
    for i in range(0, len(val)):
        total += val[i]
        if i == 0:
            maior = menor = val[i]
        if val[i] > maior:
            maior = val[i]
        elif val[i] < menor:
            menor = val[i]
    media = total / len(val)
    msg = f'Total faturamento: {total:.2f}\nMaior faturamento: {maior:.2f}\nMenor faturamento: {menor:.2f}\nFaturamento médio: {media:.2f}'
    print('=-'*45)
    return msg
    
#help(analise_faturamento)
faturas = list()
while True:
    faturas.append(float(input('Digite um faturamento: R$')))


    if int(input('deseja continuar? 1-sim/qualquer número-não\n')) != 1:
        break
print(analise_faturamento(faturas))