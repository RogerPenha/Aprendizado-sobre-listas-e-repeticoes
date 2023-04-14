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
