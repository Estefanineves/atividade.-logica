#Numeros primos-Peça ao usuario um numero inteiro e informe se ele é primo ou não
n = int(input("Digite um número: "))
primo = True
for i in range(2, n):
    if n % i == 0:
        primo = False
        break
if primo and n > 1:
    print("É primo")
else:
    print("Não é primo")