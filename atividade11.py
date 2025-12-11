#Fatorial – Peça ao usuário um número inteiro e calcule o seu fatorial (exemplo: 5! = 120).
num = int(input("Digite um número inteiro: "))
fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print(f"O fatorial de {num} é {fatorial}")