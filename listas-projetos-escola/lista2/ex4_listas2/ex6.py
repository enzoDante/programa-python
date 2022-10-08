escola = list()
aluno = list()

while True:
    nome = input('Digite um nome: ')
    matr = int(input('Digite sua matrícula: '))
    nota = float(input('Digite sua nota: '))
    while nota < 0 or nota > 10:
        nota = float(input('Digite sua nota(deve ser entre 0 e 10!): '))
    nota2 = float(input('Digite sua segunda nota: '))
    while nota2 < 0 or nota > 10:
        nota2 = float(input('Digite sua 2º nota(deve ser entre 0 e 10!): '))

    aluno.append(nome)
    aluno.append(matr)
    aluno.append(nota)
    aluno.append(nota2)

    escola.append(aluno[:])
    aluno.clear()

    escolha = input('Inserir mais alunos? s/n\n')
    escolha = escolha.upper()
    while not escolha == 'S' and not escolha == 'N':
        escolha = input('Digite ==> s/n\n')
    
    if escolha == 'N':
        break
matricula = int(input('\n\nDigite uma matrícula para saber a média: '))
for aluno in escola:
    if matricula == aluno[1]:
        media = (aluno[2] + aluno[3]) / 2
        print(f'Nome = [{aluno[0]}]\nMédia final = {media:.1f} ')