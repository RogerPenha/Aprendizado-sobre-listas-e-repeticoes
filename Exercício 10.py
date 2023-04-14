print('insira um número')
PrimeiroInteiro = int(input())
print('insira um número')
SegundoInteiro = int(input())

print('algarismo entre os dois valores:')
if PrimeiroInteiro < SegundoInteiro:
    while PrimeiroInteiro != SegundoInteiro:
        PrimeiroInteiro += 1
        if PrimeiroInteiro != SegundoInteiro:
            print(PrimeiroInteiro)
else: 
    while SegundoInteiro != PrimeiroInteiro:
        SegundoInteiro += 1
        if SegundoInteiro != PrimeiroInteiro:
            print(SegundoInteiro)