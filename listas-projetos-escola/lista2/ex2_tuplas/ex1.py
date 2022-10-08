num = ('Zero', 'Um', 'Dois', 'Três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

n = int(input('Digite um número entre 0 e 10\n'))
while n < 0 or n > 10:
    n = int(input('Digite corretamente um número entre 0 e 10!!! \n'))
print("==--"*20)
print(num[n])
print("==--"*20)