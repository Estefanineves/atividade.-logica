#sequencia de Fibonacci-exiba os 10 primeiros termo da sequencia de Fibonacci.
a, b = 0, 1
contador = 0
while contador < 10:
    print(a)
    a , b = b , a+b 
    contador += 1 