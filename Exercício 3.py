CondiçãoNome = False
CondiçãoIdade = False
CondiçãoSalário = False
CondiçãoSexo = False
CondiçãoEstadoCivil = False

while CondiçãoNome != True:
    print('Digite o seu nome:')
    Nome = input()
    if len(Nome) > 3:
        print('Nome inserido com sucesso')
        CondiçãoNome = True
    else:
        print('Nome inválido')

while CondiçãoIdade != True:
    print('Digite a sua idade:')
    Idade = int(input())
    if Idade >= 0 and Idade <= 150:
        print('Idade inserida com sucesso')
        CondiçãoIdade = True
    else:
        print('Idade inválida')

while CondiçãoSalário != True:
    print('Digite o seu salário:')
    Salário = int(input())
    if Salário >= 0:
        print('Salário inserida com sucesso')
        CondiçãoSalário = True
    else:
        print('Salário inválido')

while CondiçãoSexo != True:
    print('Digite o seu gênero: m para masculino e f para feminino:')
    Sexo = input()
    if Sexo == 'm' or Sexo == 'f':
        print('Genêro inserido com sucesso')
        CondiçãoSexo = True
    else:
        print('Genêro inválido')

while CondiçãoEstadoCivil != True:
    print('Digite o seu estado civil: s para solteiro,c para casado,v para viúvo(a) e d para divorciado:')
    EstadoCivil = input()
    
    if EstadoCivil == 's' or EstadoCivil == 'c' or EstadoCivil =='v' or EstadoCivil == 'd':
        print('Estado civil inserido com sucesso')
        CondiçãoEstadoCivil = True
    else:
        print('Estado civil inválido')

