
valor = 0

while(valor == 0):
    print('Insira um valor de 1 a 10')
    entradatemp = int(input())
    if entradatemp >= 0 and entradatemp <= 10:
        valor = 1
    else:
        print('Valor Inválido')

