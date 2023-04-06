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

