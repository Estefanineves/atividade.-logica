#Tabuada – Solicite ao usuário um número e exiba a tabuada desse número (de 1 a 10).
n=int(input("tabuada do: "))
a=1
while(a<=10):
    print(n,"x",a,"=",n*a)
    a+=1