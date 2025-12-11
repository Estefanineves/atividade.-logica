#Menu interativo – Crie um menu com opções (1) Somar dois números (2) Subtrair dois números (3) Sair. Use 'while' para repetir até sair.while True:
print("menu")
print("1 para somar")
print ("2 para subtrair ")
print ("3 para sair")

opção = int(input("escolha uma opção"))
a= int(input("primeiro"))
b= int(input("segundo"))

resultado = a+b if opção == 1 else a-b
print ("resultado  é", resultado)
elif opção ==3:
