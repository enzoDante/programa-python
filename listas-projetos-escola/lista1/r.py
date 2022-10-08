a = int(input("candidato A-votos: "))
b = int(input("candidato B-votos: "))
c = int(input("candidato C-votos: "))
vn = int(input("Votos nulos: "))
vb = int(input("Votos em branco: "))

voto_valido = a+b+c
total = voto_valido + vn + vb

perct = (voto_valido*100)/total
perca = (a*100)/total
percb = (b*100)/total
percc = (c*100)/total
percn = (vn*100)/total
percb = (vb*100)/total

print(f'total de votos: {total}\nporcentagem total: {perct}\nporcentagem de A {perca}\nporcentagem de b: {percb}\nporcentagem de C: {percc}\nporcentagem de nulos: {percn}\nporcentagem de brancos: {percb}')
