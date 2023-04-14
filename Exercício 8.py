números = [42,3,18,24,56]
contador = 0
Soma = 0
Média = 0

while (contador < len(números)):
    Soma += números[contador]
    contador += 1
Média = Soma/len(números)
print('Soma dos números:' + str(Soma))
print('Média da soma dos números:' + str(Média))
