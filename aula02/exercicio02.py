nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua primeira nota: "))
nota3=  float(input("Digite sua primeira nota: "))

media = (nota1+nota2+nota3)/3

if media > 4:

    if media >= 7:
     print("aprovado")
    else:
     print("recuperação")
else:
    print("reprovado")

if media < 7:
    if media > 4:
        print("recuperação")
    else:
        print("reprovado")
else:
    print("aprovado")
