a = int(input("Digite 1º valor: "))
b = int(input("Digite 2º valor: "))
c = int(input("Digite 3º valor: "))
d = int(input("Digite 4º valor: "))

soma = (a + b) + (a+c) + (a+d) + (b+c) + (b+d) + (c+d)
mult = (a * b) * (a*c) * (a*d) * (b*c) * (b*d) * (c*d)
print(f'soma = {soma}, multiplicação = {mult}')

