soma_pares = 0
soma_impares= 0 
for i in range (10):
 num = int (input ( "digite um numero inteiro :"))
if num % 2 == 0:
 soma_pares += num 

else:
 soma_impares=+ num 

 print("A soma dos números pares é:", soma_pares)
print("A soma dos números ímpares é:", soma_impares)