n_notas = int(input("Digite a quantidade de notas: "))
nota = 0

for i in range(n_notas):
    nota += int(input("Digite a nota:" ))
   
media = nota/n_notas
print("Soma das notas: ",nota)
print("Média: ", media)