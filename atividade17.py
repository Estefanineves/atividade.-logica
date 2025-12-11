#Média de idades – Leia a idade de várias pessoas (até que o usuário digite 0). Mostre a média das idades digitadas.
soma = 0
contador = 0

idade = int(input("Digite a idade (0 para sair): "))
while idade != 0:
    soma += idade
    contador += 1
    idade = int(input("Digite a idade (0 para sair): "))

if contador > 0:
    print(f"A média das idades é {soma / contador:.2f}")
else:
    print("Nenhuma idade foi digitada.")