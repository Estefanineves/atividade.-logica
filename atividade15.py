# Leitura até número negativo – Leia vários números e pare quando o usuário digitar um número negativo. Exiba a soma dos números positivos.
soma = 0
while True:
    n = int(input("digite um numero: "))
    if n < 0:
        break
    soma += n
print("soma dos positivos =", soma)