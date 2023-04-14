números = [1,15,800,4,20]
MaiorNúmero = 0
contador = 0

while (contador != len(números)):
    if MaiorNúmero < (números[contador]):
        MaiorNúmero = (números[contador])
    contador += 1
print('O maior número da lista é:' + str(MaiorNúmero))