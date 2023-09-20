pergunta = ''
while pergunta in "Ss":
    numeroUm = float(input("digite sua nota: "))
    while (numeroUm < 0 or numeroUm >10):
        numeroUm = float(input("Por favor Digite uma nota valida: "))

    numeroDois = float(input("digite sua nota: "))
    while (numeroDois < 0 or numeroDois >10):
        numeroDois = float(input("Por favor Digite uma nota valida: "))
    print((numeroUm+numeroDois)/2)
    pergunta = input("Quer fazer um novo calculo?(s/n) ")


