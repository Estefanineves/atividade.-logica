#Maior e menor número – Leia 10 números e determine o maior e o menor valor digitado.
num = int(input("Digite o um número: "))
maior = menor = num

for i in range(2, 11):
    num = int(input(f"Digite o {i} número: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("Maior número:", maior)
print("Menor número:", menor)