#Produto dos números – Leia 10 números inteiros e calcule o produto (multiplicação) de todos eles.
produto = 1
i = 0

while i < 10:
    num = int(input(f"Digite o  número: "))
    produto *= num
    i += 1

print("O produto de todos os números é:", produto)
