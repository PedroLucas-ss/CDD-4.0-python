turma = ["","","","",""]
somaTurma =0
mediaMaior = 0

for i in range(5):
    addTurma = float(input(f"Qual a nota do {i+1} aluno: "))
    turma[i] = addTurma

for x in range(5):
    somaTurma +=turma[x]

mediaTurma = somaTurma/5

for z in range(5):
    if turma[z] >= mediaTurma:
        mediaMaior += 1


print('Media da turma = ', mediaTurma)
print('Alunos que obtiveram nota maior ou igual que a media: ', mediaMaior)
