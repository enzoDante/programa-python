while True:
    try:
        x = int(input('Digite um número inteiro: '))
        y = float(input('Digite um número real: '))
    except (ValueError):
        print('!-'*30)
        print('NÃO digite outro valor além do que se pede!!!')
        print('!-'*30)
    #except Exception as erro:
        #print(erro,' teste')
    else:
        break
    