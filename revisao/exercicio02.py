cotinue  = "S"

while cotinue in "Ss":
    num = int(input("Digite um numero: "))
    while num == 0:
        num = int(input("Por favor, Digite um numero diferente de zero: "))
    else:
        if num > 0:
            print("positivo")
        else:
            print("negativo")
        cotinue = input("Deseja testar outro numero? ")