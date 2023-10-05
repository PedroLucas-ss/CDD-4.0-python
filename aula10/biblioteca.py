def soma(n1, n2):
    resultado = n1 + n2
    print(f'A soma de {n1} e {n2} = {resultado}')


def subtrair(n1, n2):
    resultado = n1 - n2
    print(f'A subtração de {n1} - {n2} = {resultado}')


def multi(n1, n2):
    resultado = n1 * n2
    print(f'A multiplicação de {n1} x {n2} = {resultado}')


def div(n1, n2):
    resultado = n1 / n2
    print(f'A divisãoo de {n1} / {n2} = {resultado}')

def menu ():
     print("=========MENU======== \n 1- somar \n 2- subtrair \n 3- dividir \n 4- multiplicar\n s- sair  \n=====================\n")

def piramideNumerica(num):
    if num in '1234567890':
        for i in range(num+1):
            print(str(i) * i)
            print()
    else:
        numRep = int(input("quantas vezes vc deseja repetir esse caracter? "))
        for i in range(numRep+1):
            print(num*i)
def piramideNum(num):
    for i in range(num+1):
        for x in range(i):
            print(x+1, end='')
        print()

def vogais(texto):
    contVogais = 0
    contEspacos =0
    for i in texto:
        if i in 'aeiouAEIOU':
            contVogais+=1
        if i == " ":
            contEspacos +=1
    print(f"Vogais: {contVogais}")
    print(f'Espaços: {contEspacos}')

def estoque(produto,quant,valor_uni):
    valor_total = quant * valor_uni
    return valor_total