import webbrowser as wb
#os dois abaixo abre tab
#webbrowser.open('http://opera.com', new=2)
#wb.open_new_tab('http://www.google.com')
x = int(input("1-Anime House\n2-Anime Ups\n3-Lista anime\n"))
while x < 1 or x > 3:
    x = int(input("escolha 1/2/3!!!\n\n"))

if x == 1:
    wb.open('https://animeshouse.net')
elif x == 2:
    wb.open('https://animesup.biz')
else:
    wb.open('https://docs.google.com/spreadsheets/d/1l1I4JTJ60KFCNdSAk6xM5eGMPAGhoHX8y17jW-Awbz4/edit?usp=sharing')