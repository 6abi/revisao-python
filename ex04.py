def soma(n1 ,n2):
    soma = n1 + n2
    return soma

def sub(n1,n2):
    sub = n1 - n2
    return sub

def mult(n1,n2):
    mult = n1 * n2
    return mult

def divisao(n1,n2):
    divisao = n1 / n2
    return divisao

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

print("Soma: ",soma(n1,n2))
print("Subtração: ",sub(n1,n2))
print("Multiplicação: ",mult(n1,n2))
print("Divisão: ",divisao(n1,n2))
   
