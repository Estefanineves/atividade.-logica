#Desafio final – Leia vários números (parando com 0) e mostre: a quantidade de números digitados, a média, o maior e o menor número e quantos foram pares.
numeros = []
while (n := int(input("Digite um número (0 para sair): "))) != 0:
    numeros.append(n)

if numeros:
    print(f"Quantidade: {len(numeros)}")
    print(f"Média: {sum(numeros)/len(numeros):.2f}")
    print(f"Maior: {max(numeros)}")
    print(f"Menor: {min(numeros)}")
    print(f"Pares: {sum(1 for x in numeros if x % 2 == 0)}")
else:
    print("Nenhum número foi digitado.")