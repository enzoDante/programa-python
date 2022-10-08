sm = float(input("Digite seu salário mensal: "))
pr = float(input("Percentual de reajuste: "))
ns = sm - ((pr * sm) / 100)
print(f'novo salário = R$ {ns:.2f}')
