Números = [3,5,9,4,7]
print(Números)

def Soma(Números):
    soma = 0
    for i in Números:
        soma = soma + i
    return soma
print(Soma(Números))

def Multiplicação(Números):
    multiplicação = 1
    for i in Números:
        multiplicação *= i
    return multiplicação
print(Multiplicação(Números))
