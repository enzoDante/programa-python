from reportlab.pdfgen import canvas
#permite uso do método registerFont()
from reportlab.pdfbase import pdfmetrics
#importando método ttfonts, reconhece uma fonte true-type
from reportlab.pdfbase.ttfonts import TTFont

def regua(pdf):
    #cor da fonte
    pdf.setFillColor('red')
    
    for coluna in range(0, 595, 5):
        pdf.setFont("Helvetica-Oblique", 2)
        #numero das colunas na última linha 'linha 0'
        pdf.drawString(coluna, 0, f'{coluna}')

    for linha in range(0, 841, 5):
        pdf.setFont("Helvetica-Oblique", 2)
        #linhas na primeira coluna 'coluna 0'
        pdf.drawString(0, linha, f'{linha}')


def gerarpdf(dicionario):
    try:
        nomearquivo = input('Digite um nome p arquivo:  ')
        #criando objeto pdf
        pdf = canvas.Canvas(f'{nomearquivo}.pdf')
        
        #cria uma régua no pdf, p ajudar o programador
        regua(pdf)
        
        #cor da fonte do pdf
        pdf.setFillColor('black')
        #defini texto do titulo
        pdf.setTitle('Relatório titulooo')
        #nome da fonte e tamanho para texto em diante
        pdf.setFont("Helvetica-Oblique", 16)

        #linha e coluna são ao contrário de linha e coluna de matriz
        #linha 750 e coluna 10
        pdf.drawString(274, 750, 'Relll profsss 2 ano')

        pdf.setFont('Arial', 14)
        pdf.drawString(10, 720, 'Nome proff')
        x = 700 #medida em mm milimetros
        for nome, disciplina in dicionario.items():
            print(f'{nome} | {disciplina} ')
            x -= 20 #-20mm
            pdf.drawString(10, x, f'{nome} e sua {disciplina} ')
        
        #criando o pdf
        pdf.save()
        print(f'{nomearquivo} foi criado ')


    except:
        print('deu erro man')


#registrando a fonte arial
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

dicionario = {'Alberson': 'pooi', 'Bruno':'banco dados', 'Helio':'chato p carai', 'wagner':'babaca da porra'}
gerarpdf(dicionario)