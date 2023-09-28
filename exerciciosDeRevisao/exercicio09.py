import os

while True:
    numero = int(input("Digite o numero"))
    antecessor = numero - 1
    sucessor = numero + 1
    print("==================MENU=================")
    print("1 - antecessor")
    print("2 - sucessor")
    print("3 - sair ")
    resp = (input("Digite a opcao: "))
    if resp == '1':
        print(antecessor)
    elif resp == '2':
        print(sucessor)
    elif resp == '3':
        print("saindo do sistema")
        break
    else:
        print("opcao invalida")

