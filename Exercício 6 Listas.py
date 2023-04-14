NotasAlunos = [["Caio",[10,9,4,21]],["Roger",[10,10,10,10]],["Matheus",[0,0,0,0]],["Flavinho",[7,8,9,7]],["ManoBrown",[8,5,4,7]],["Flavinho do Pneu",[3,6,7,10]],["Paulinho",[9,5,3,6]],["Jacinto Leite no Rego",[10,6,3,4]],["Deide Costa",[5,10,2,9]],["Luiz Inácio",[2,4,3,6]]]

def CalcularMédia(lista):
    soma = 0
    for i in lista:
        soma += i
        media = soma/len(lista)
    return media


def organizar(NotasAlunos):
    mediasdosalunos = []
    for i in NotasAlunos:
        mediasdosalunos.append(CalcularMédia(i[1]))
    return mediasdosalunos


def aprovados(NotasAlunos):
    AlunosAprovados = []
    for i in organizar(NotasAlunos):
        if i >= 7:
            AlunosAprovados.append(i)
            aprovados= len(AlunosAprovados)
    return aprovados
        
        
print('Média dos alunos:' + str(organizar(NotasAlunos)))

print('Quantidade de alunos aprovados:' + str(aprovados(NotasAlunos)))
