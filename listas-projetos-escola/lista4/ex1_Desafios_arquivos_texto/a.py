while True:
    try:
        nomearquivo = input("Insira o nome do arquivo a ser criado:  ")
        arquivo = open(f'D:/codigo-vsCode/programa-python/listas-projetos-escola/lista4/ex1_Desafios_arquivos_texto/{nomearquivo}.html', 'x')

        titulo = input('Digite um título para sua página:  ')
        texto = input("Digite seu texto:\n")

        if not texto.startswith('<p>') and not texto.endswith('</p>'):
            texto = f'<p>{texto}</p>'

        formatacao_html = f'''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
</head>
<body>
    <header><h1>{titulo}</h1></header>
    <main>
        {texto}
    </main>
</body>
</html>
        '''
        arquivo.write(formatacao_html)
        arquivo.close()
        print("Arquivo gravado com sucesso!")
    except:
        print("Ocorreu um erro ao criar o arquivo! verifique se o arquivo ja existe!\n")
    finally:
        if input('Deseja continuar? 1-sim qualquer tecla-não') != '1':
            break
