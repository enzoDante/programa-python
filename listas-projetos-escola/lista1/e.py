valor = float(input("Digite o valor a ser pago: "))
taxa = float(input("Digite a taxa a ser cobrado: "))
tempo = float(input("Digite o tempo: "))
pres = valor + (valor * taxa/100) * tempo

print(f'prestação = {pres}')