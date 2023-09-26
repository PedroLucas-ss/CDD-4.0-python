
continuar = 's'
while continuar in "Ss":
    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a primeira nota: "))

    media = (nota1+nota2)/2

    if media >= 7:
        print("APROVADO")
    elif media >= 4:
        print("VAI PARA CLINICA")
    else:
        print("FOTO COM O PROF")

    print(f'Sua media é {media}')
    continuar = input("Deseja refazer a media(s/n): ")

