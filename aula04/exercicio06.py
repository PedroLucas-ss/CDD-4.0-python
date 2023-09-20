alunos = int(input("Digite o numero de alunos: "))
i = 0
somaNotas = 0
while i < alunos:
    nota = float(input("Digite a nota: "))
    somaNotas += nota
    i+= 1

mediaTurma =  somaNotas/alunos
print("media: ", mediaTurma )