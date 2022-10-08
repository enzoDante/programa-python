# 2HID - Enzo Dante, Samuel Pascoal e Bruno Braga
#projeto 1º bimestre

total_iluminacao = total_lampadas = 0

while True:
    print("Quarto/Sala de TV = 1 | Salas/Cozinhas/Varandas = 2 | Escritório/Banheiro = 3")
    comodo = int(input("Escolha uma opção:\n"))
    while comodo < 1 or comodo > 3:
        comodo = int(input("Digite um número da classe do cômodo (1 - 2 - 3)\n"))

    largura = float(input("Digite a largura do cômodo: "))
    while largura < 1:
        largura = float(input("Digite a largura do cômodo: "))

    comprimento = float(input("Digite o comprimento do cômodo: "))
    while comprimento < 1:
        comprimento = float(input("Digite o comprimento do cômodo: "))
    

    area = largura * comprimento
    if comodo == 1:
        print('Quarto/Sala de TV')
        iluminacao = area * 15
        print('\nPotência de iluminação por metros quadrados = 15w')
    elif comodo == 2:
        print('Salas/Cozinhas/Varandas')
        iluminacao = area * 18
        print('\nPotência de iluminação por metros quadrados = 18w')
    elif comodo == 3:
        print('Escritório/Banheiro')
        iluminacao = area * 20
        print('\nPotência de iluminação por metros quadrados = 20w')

    
    lampadas = iluminacao/60
    
    arredondar = int(lampadas) #caso tenha nº decimais, deverá arredondar!!!
    if lampadas - arredondar != 0:
        arredondar += 1 #aq irá arredondar
        lampadas = arredondar
    
    total_iluminacao += iluminacao
    total_lampadas += lampadas
    
    print(f'Área do comodo = {area} metros quadrados\n\nPotência de iluminação = {iluminacao}W\n\n')
    print(f'Lampadas necessárias = {lampadas:.0f}')
    
    r = str(input("Deseja continuar inserindo comodos? s/n\n"))
    while r != 's' and r != 'n':
        r = str(input("Deseja continuar inserindo comodos? s/n\n"))
    if r == 'n':
        break

print(f'Total de lampadas necessária para a residência = {total_lampadas:.0f}')
print(f'Total de potência necessária = {total_iluminacao}')





