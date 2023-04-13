#exercício 1

'''Lista1 = []
append.Lista1(2)
append.Lista1(5)


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

#exercício 4

Lista4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
vogais = ['a','e','i','o','u']
ListadeConsoantes = []
consoantes = 0
contador = 0
for i in Lista4:
        if not  Lista4 [contador] in vogais:
            consoantes+=1
            ListadeConsoantes.append(Lista4[contador])
        contador += 1
print(ListadeConsoantes)
print (consoantes)


#exercício 5

Lista5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Pares = []
Impares = []
contador = 0

for i in Lista5:
    if Lista5 [contador]%2:
        Impares.append(Lista5[contador])
    else:
        Pares.append(Lista5[contador])
    contador+= 1
print("números totais",Lista5)
print ("números pares:",Pares)
print ("números impares:",Impares)

#Exercício 7

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

#exercício 8

idades = []
alturas = []
for i in range(0,5):
    print('digite uma idade')
    idade = input()
    print('digite uma altura em metros')
    altura = input()
    idades.append(idade)
    alturas.append(altura)

idades.reverse()
alturas.reverse()

contador = 0

for i in idades:
    print('Usúario' + str(contador + 1) + ':')
    print('idade' + str(i))
    print('altura' + str(alturas[contador]))
    contador += 1

#Exercício 9

lista9 = [50,100,150,200,250,300,350,400,450,500]

def SomaDeTodosOsQuadrados(inteiros):
    soma = 0
    for i in inteiros:
        soma += i * i
    return soma
    
print('lista dos números:' + str(lista9))
print('soma de todos os números ao quadrado:' + str(SomaDeTodosOsQuadrados(lista9)))'''

ListaVetorA = [1,2,3,4,5,6,7,8,9,10]
ListaVetorB = [11,12,13,14,15,16,17,18,19,20]
ListaVetorC = []

contador = 0
for i in ListaVetorA:
    ListaVetorC.append(i)
    ListaVetorC.append(ListaVetorB[contador])
    contador += 1
    print (ListaVetorC)


