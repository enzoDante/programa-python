nome = input('Digite um nome:\n')

x = nome.count('a') + nome.count('A')
print(f'{x} letra(s) a/A encontrado')
if x > 0:
    print(f'{nome.find("A")}º posição tem a letra "A"')
    print(f'{nome.rfind("A")}º posição tem a última letra "A"')