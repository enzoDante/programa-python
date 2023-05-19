frase = input('Digite uma frase:\n')
frase = frase.strip() #tira espacos do comeco e do final da string

print(frase.upper())
print(frase.lower())
print(f'{len(frase)} letras')
"Minha Frase PyThon"

f = frase.split() #quebra em array (lista)
print(f"{len(f[0])} letras na primeira palavra")
