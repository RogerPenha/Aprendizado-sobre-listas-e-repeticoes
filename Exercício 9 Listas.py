lista9 = [50,100,150,200,250,300,350,400,450,500]

def SomaDeTodosOsQuadrados(inteiros):
    soma = 0
    for i in inteiros:
        soma += i * i
    return soma
    
print('lista dos números:' + str(lista9))
print('soma de todos os números ao quadrado:' + str(SomaDeTodosOsQuadrados(lista9)))