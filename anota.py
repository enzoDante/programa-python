print('Olá mundo!')

print("""texto aleatório para ocupar
mais de uma linha usando 3 aspas duplas
desta forma aq msm""")

print('a linha abaixo esta na frente',end=' ')
print('estou do lado na liha acima :)')

a = " Olá mundo"
x = 5
print(a*x) #printar "Olá mundo" 5 vezes

x = input("digite um número:\n")
x = int(input("Digite um número:\n"))
a = str(input("Escreva algo: "))
b = float(input("Digite uma altura: "))

if x == 10:
    print(f"é igual a {x}")
elif x > 10:
    print(f"é maior q 10 {x}")
else:
    print(f"é menor q 10 {x}")

if x > 10 and x != 15:
    print(f"{x} é maior que 10 e diferente de 15")

if b < 1 or b > 3:
    print(f"{b} é uma altura diferenciada")

a = "Olá mundo!"
for con in a:
    print(f"{con}")


