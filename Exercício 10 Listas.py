ListaVetorA = [1,2,3,4,5,6,7,8,9,10]
ListaVetorB = [11,12,13,14,15,16,17,18,19,20]
ListaVetorC = []

contador = 0
for i in ListaVetorA:
    ListaVetorC.append(i)
    ListaVetorC.append(ListaVetorB[contador])
    contador += 1
    print (ListaVetorC)