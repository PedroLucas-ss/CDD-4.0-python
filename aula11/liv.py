def tipodenum(num):
    if num > 0:
        return 'P'
    elif num < 0:
        return 'N'
    else:
        return 'z'
def media(nota1,nota2):
    med = (nota1 + nota2)/2
    return med

def status(m):
    if m >= 7:
        print(f"Aprovado media:{m}")
    else:
        print(f"Reprovado media: {m}")

def soma(*args):
    soma = 0
    cont = 0
    addArray = 0
    for x in args:
        cont +=1
    arrayTest= [0]*cont
    for i in args:
        soma += i
        arrayTest[addArray] = i
        addArray += 1
    return soma, arrayTest


def textSize(texto):
    cont = 0
    contArray = 0
    for i in texto:
        if texto != ' ':
            cont += 1
        contArray += 1


    return montarArray, arraySrep



