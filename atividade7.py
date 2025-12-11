#Média de notas – Peça ao usuário para informar 5 notas e calcule a média final.
soma = 0
i = 0

while i < 5:
    nota = float(input(f"Nota {i+1}: "))
    soma += nota
    i += 1

print("Média final:", soma / 5)