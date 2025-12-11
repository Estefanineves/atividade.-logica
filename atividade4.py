#Soma dos números de 1 até N – Peça ao usuário para digitar um número n e calcule a soma de todos os números de 1 até n.
n = int(input ("digite um numero inteiro : "))

soma=0
for i in range(1,n +1):
    soma += i
    print(f"a soma de 1 ate  {n} é {soma}")