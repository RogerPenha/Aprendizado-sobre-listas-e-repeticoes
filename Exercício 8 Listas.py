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
