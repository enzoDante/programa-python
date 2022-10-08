from datetime import date


from datetime import date
trabalhador = dict()

trabalhador['nome'] = input('Digite o nome do trabalhador: ')
trabalhador['nasceu'] = int(input('Digite o ano de nascimento: '))
trabalhador['anos_trabalhou'] = int(input('Digite o ano que começou a trabalhar: '))


trabalhador['idade'] = date.today().year - trabalhador['nasceu']
trabalhador['anos_trabalhou'] = date.today().year - trabalhador['anos_trabalhou']
print(trabalhador)

aposento = dict()
aposento['nome'] = trabalhador['nome']
aposento['idade'] = trabalhador['idade'] + 30
aposento['anos_aposentar'] = 30 - trabalhador['anos_trabalhou']
if aposento['anos_aposentar'] < 0:
    aposento['anos_aposentar'] = aposento['anos_aposentar'] * (-1)

for i, v in aposento.items():
    print(f'[{i}] ==> [{v}] ')