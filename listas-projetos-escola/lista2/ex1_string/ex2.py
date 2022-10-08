n = int(input('Digite um número:  '))
while n < 0 or n > 9999:
    n = int(input('Digite um número entre 0 e 9999:   '))
    
unidade = n % 10  # 5489 -- 9

num = (n - unidade)/10 #5489 - 9 -> 5480 / 10 = 548
dezena = num % 10 #548 -- 8

num = (num - dezena) / 10 #548 - 8 -> 540 / 10 = 54
centena = num % 10 #54 -- 4

num = (num - centena) / 10  #54 - 4 -> 50 / 10
milhares = num % 10 #5

print(f'{milhares} --- {centena} --- {dezena} --- {unidade}')