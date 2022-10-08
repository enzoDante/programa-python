from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = num[0]
menor = num[0]
for i in num:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i
        
print("==--"*20)
print(f'números sorteados = {num}\nmaior = {maior}\nmenor = {menor}')
#max(num) min(num)