num = (int(input('Digite 1º número: ')), int(input('Digite 2º número: ')),
int(input('Digite 3º número: ')), int(input('Digite 4º número: ')), int(input('Digite 5º número: ')))

print("==--"*20)
print("\n",num, "\n")
print("==--"*20)
print(f'quantidade de número 10 digitado = {num.count(10)} ')
print("==--"*20)
if num.count(3) > 0:
    print(f'posição do 1º número 3 = {num.index(3)+1}ª posição')
    print("==--"*20)
else:
    print('Não existe número 3 na tupla!!!')
    print("==--"*20)
    
print('números pares:')
for par in num:
    if par % 2 == 0:
        print(par)