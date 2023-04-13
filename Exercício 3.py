Notas = {8,5,4,10,7}

def CalcularNotas (Notas):
    QuantidadeDeNotas = len(Notas)
    Média = sum(Notas) / QuantidadeDeNotas
    return Média
print(CalcularNotas(Notas))