'''
r  - ler se existe arquivo
r+ - cria e le arquivo
w  - cria arquivo e deleta o conteudo antigo
a  - append(nova linha em um arquivo existente)
x  - cria arquivo caso n exista (se existir dara erro)
'''
try:
    arquivo = open('D:/codigo-vsCode/programa-python/listas-projetos-escola/lista4/av.txt', 'a')
    cont = input('digite\n')
    arquivo.write(f'{cont}\n')
    arquivo.close()
except:
    print('erro')