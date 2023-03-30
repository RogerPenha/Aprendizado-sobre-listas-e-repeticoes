#exercício 1

Lista1 = [1,2,3,4,5]
print(Lista1)

#exercício 2

Lista2 = [1,2,3,4,5]
Lista2.reverse()
print(Lista2)

#exercício 3

Notas = {8,5,4,10,7}

def CalcularNotas (Notas):
    QuantidadeDeNotas = len(Notas)
    Média = sum(Notas) / QuantidadeDeNotas
    return Média
print(CalcularNotas(Notas))
