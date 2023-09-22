alunosQuant = int(input("Quantos alunos tem na sala? "))
alunos = []
for i in range(alunosQuant):
   ateste = (input(f'Digite o nome do {i} aluno: '))
   alunos.append(ateste)
for x in alunos:
    print(x)