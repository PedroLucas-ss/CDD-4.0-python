alunosQuant = int(input("Quantos alunos tem na sala? "))
alunos = []
for i in range(alunosQuant):
   teste = (input(f'Digite o nome do {i} aluno: '))
   alunos.append(teste)
for x in range(alunosQuant):
    print(alunos[x],x)