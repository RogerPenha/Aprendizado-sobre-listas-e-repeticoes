Condição = False

while Condição != True:
    print('digite o Usuário:')
    Usuário = input()
    print('digite a senha:')
    Senha = input()
    if Senha != Usuário:
        print('Acessado com Sucesso')
        Condição = True
    else:
        print('Senha e usuário inválidos')