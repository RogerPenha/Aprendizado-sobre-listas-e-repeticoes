condição = False

while condição != True:
    print('Insira a população do País A:')
    PaísA = int(input())
    print('insira a taxa de crescimento do País A')
    TaxadeCrescimentoA = float(input())
    print('insira a população do País B:')
    PaísB = int(input())
    print('insira a taxa de crescimento do País B')
    TaxadeCrescimentoB = float(input())
    PopulaçãoA = PaísA * TaxadeCrescimentoA
    PopulaçãoB = PaísB * TaxadeCrescimentoB
    print('População so País A:',PopulaçãoA)
    print('População do País B:',PopulaçãoB)
    print('insira "sair" para sair ou "repetir" para repetir a operação')
    entradatemp = input()
    if entradatemp == 'sair':
        condição = True
    if entradatemp == 'repetir':
        condição = False