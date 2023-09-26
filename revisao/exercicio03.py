cont = 's'

while cont in "Ss":
    idade = int(input("Digite sua idade: "))
    mesNasc = int(input("Digite o numero do mes que voce nasceu"))
    anoAtual = int(input("Em qual ano vc esta"))
    mesAtual = int(input("Em qual mes vc esta"))

    if mesNasc> mesAtual:
        anoNasc = (anoAtual-1) - idade
    else:
        anoNasc = anoAtual - idade

    print(anoNasc)
    cont = input("deseja continuar? ")