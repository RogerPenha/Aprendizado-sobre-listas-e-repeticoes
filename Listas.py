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

#exercício 6

Alunos = 'aluno1','aluno2','aluno3','aluno4','aluno5','aluno6','aluno7','aluno8','aluno9','aluno10'

aluno1=[7,3,10,7]
aluno2=[2,9,3,1]
aluno3=[4,6,2,10]
aluno4=[1,7,10,5]
aluno5=[10,8,7,9]
aluno6=[3,10,6,4]
aluno7=[10,4,4,6]
aluno8=[10,10,8,9]
aluno9=[8,5,2,10]
aluno10=[10,5,7,1]
notas = 0.0


SomaAluno1 = sum(aluno1)
SomaAluno2 = sum(aluno2)
SomaAluno3 = sum(aluno3)
SomaAluno4 = sum(aluno4)
SomaAluno5 = sum(aluno5)
SomaAluno6 = sum(aluno6)
SomaAluno7 = sum (aluno7)
SomaAluno8 = sum(aluno8)
SomaAluno9 = sum (aluno9)
SomaAluno10 = sum(aluno10)

MédiaAluno1 = SomaAluno1 / len(aluno1)
MédiaAluno2 = SomaAluno2 / len(aluno2)
MédiaAluno3 = SomaAluno3 / len(aluno3)
MédiaAluno4 = SomaAluno4 / len(aluno4)
MédiaAluno5 = SomaAluno5 / len(aluno5)
MédiaAluno6 = SomaAluno6 / len(aluno6)
MédiaAluno7 = SomaAluno7 / len(aluno7)
MédiaAluno8 = SomaAluno8 / len(aluno8)
MédiaAluno9 = SomaAluno9 / len(aluno9)
MédiaAluno10 = SomaAluno10 / len(aluno10)

Médias= [MédiaAluno1,MédiaAluno2,MédiaAluno3,MédiaAluno4,MédiaAluno5,MédiaAluno6,MédiaAluno7,MédiaAluno8,MédiaAluno9,MédiaAluno10]


if Médias > 7:
    print()
else:
    





