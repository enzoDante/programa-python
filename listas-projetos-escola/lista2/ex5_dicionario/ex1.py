d = dict()
nome = input("Digite um nome: ")
media = float(input("Digite sua média: "))
while media < 0 or media > 10:
    media = float(input('Digite uma média válida: '))
d['nome'] = nome
d['media'] = media
if media <= 5.9:
    d['resultado'] = "Aluno em recuperação"
else:
    d['resultado'] = 'Aluno na média!'
print(d)
for v in d.values():
    print(v)