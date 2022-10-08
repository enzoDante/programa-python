numeros = list()

def verificar(valores):
    maior = menor = 0
    pmaior = pmenor = 0
    for i, v in enumerate(valores):
        if i == 0:
            maior = menor = v
            pmaior = pmenor = i
        elif v > maior:
            maior = v
            pmaior = i
        elif v < menor:
            menor = v
            pmenor = i
    print('=-'*40)
    print(f'Maior número: {maior} - na posição {pmaior}\nMenor número: {menor} - na posição {pmenor} ')


while True:
    num = int(input('Digite um número: '))
    while num in numeros:
        num = int(input('Digite um número que não foi digitado anteriormente:\n '))
    numeros.append(num)

    if int(input('deseja continuar? 1-sim/qualquer número-não\n')) != 1:
        break
verificar(numeros)