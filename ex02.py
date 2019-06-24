# Faça um programa que receba dois inputs, uma palavra/frase e uma letra.
# O programa deve retornar quantas vezes a letra apareceu na palavra/frase. Dica:
# contagem de valores .count("valor")

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")
counter = 0
counter = palavra.count(letra)
print(counter)