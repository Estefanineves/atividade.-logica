#Números ímpares em intervalo – Leia dois valores A e B e exiba todos os números ímpares entre eles.
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

# Ajusta para que a seja menor que b
if a > b:
    a, b = b, a

# Define o primeiro ímpar
inicio = a + 1 if (a + 1) % 2 != 0 else a + 2

# Imprime os ímpares usando passo 2
for numero in range(inicio, b, 2):
    print(numero, end=" ")