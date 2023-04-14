ListaVetorA = [1,2,3,4,5,6,7,8,9,10]
ListaVetorB = [11,12,13,14,15,16,17,18,19,20]
ListaVetorC = [21,22,23,24,25,26,27,28,29,30]
ListaVetorD = []

contador = 0
for i in ListaVetorA:
    ListaVetorD.append(i)
    ListaVetorD.append(ListaVetorB[contador])
    ListaVetorD.append(ListaVetorC[contador])
    contador += 1
    print (ListaVetorD)