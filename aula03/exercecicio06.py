numeroAluno = int(input("Quandos alunos tem na classe? "))
notaTotal  = 0
for i in range(numeroAluno):
    nota = float(input (f"Digite na nota do aluno:{(i+1)}º: "))
    notaTotal += nota
media =notaTotal/numeroAluno
print("A media na turma é: ", media)