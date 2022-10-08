frase = input('Digite uma frase:\n')
frase = frase.strip()

print(frase.upper())
print(frase.lower())
print(f'{len(frase)} letras')
"Minha Frase PyThon"

f = frase.split()
print(f"{len(f[0])} letras na primeira palavra")
