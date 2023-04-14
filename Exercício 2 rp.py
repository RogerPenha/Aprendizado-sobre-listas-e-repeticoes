Condição = False

while Condição != True:
    print('Usuário:')
    Usuário = input()
    print ('Senha:')
    Senha = input()
    if Usuário != Senha:
        print('Acessado com sucesso')
        Condição = True
    else:
        print('Usuário e Senha inválidos')