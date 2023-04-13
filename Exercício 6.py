NotasAlunos = [["Caio",[10,7,4,2]],["Roger",[10,10,10,10]],["Matheus",[0,0,0,0]],["Flavinho",[6,4,9,2]],["ManoBrown",[8,5,4,7]],["Flavinho do Pneu",[3,0,7,10]],["Paulinho",[9,5,3,6]],["Jacinto Leite no Rego",[10,6,3,4]],["Deide Costa",[5,10,2,9]],["Luiz Inácio",[2,4,3,6]]]

def CalcularMédia(lista):
    soma = 0
    for i in lista:
        soma += i
        media = soma/len(lista)
        media

def organizar(NotasAlunos):
    mediasdosalunos = []
    for i in NotasAlunos:
        mediasdosalunos.append(CalcularMédia(i[1]))
        mediasdosalunos

def aprovados(NotasAlunos):
    AlunosAprovados = []
    for i in organizar(NotasAlunos):
        if i >= 7:
            AlunosAprovados = len(AlunosAprovados)
            AlunosAprovados
        
        
print('Média dos alunos:' + str(organizar(NotasAlunos)))

print('Quantidade de alunos aprovados:' + str(aprovados(NotasAlunos)))
