#Contagem de múltiplos de 3 – Mostre quantos números entre 1 e 100 são múltiplos de 3.
contador = 0 
i = 1 

while i <= 100:
    if i % 3 == 0:
        contador += 1
    i += 1

print(f" entre 1 e 100, existem {contador} multiplos de 3.")