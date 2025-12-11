#Adivinhe o número – O computador deve 'pensar' em um número de 1 a 20 e o usuário deve tentar adivinhar até acertar.
numero=int(input("adivinhe o numero: "))

if numero < 5:
    print("tente um numero maior")
elif numero > 5:
    print("tente um numero menor")
else:
    print("voce acertou!")