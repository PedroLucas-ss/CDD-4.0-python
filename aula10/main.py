from biblioteca import *

while True:
    piramideNum('o rato to')
    opção = input()
    if opção in 'Ss':
        break
    n1 = int(input("Digite o valor do primeiro numero"))
    n2 = int(input("Digite o valor do segundo numero"))

    if opção == '1':
        soma(n1,n2)
    elif opção == '2':
        subtrair(n1,n2)
    elif opção == '3':
        div(n1,n2)
    elif opção == '4':
        multi(n1,n2)
    else:
        print("Opção invalida")


