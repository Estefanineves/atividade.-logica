#Contagem de números positivos – Peça para o usuário digitar 10 números e conte quantos são positivos.
positivos=0
i=0

while i < 10:
 if int(input("Digite um número: ")) > 0:
    positivos += 1
i += 1

print("Quantidade de positivos =", positivos)