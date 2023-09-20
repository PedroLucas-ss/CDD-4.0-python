i = 0
soma = 0
while i < 10:
    numero = float(input("Digite um numero: "))

    soma += numero
    soma += 1

while True:
    numero = float(input("Digite um numero: "))

    soma += numero
    i += 1
    if i == 10:
        break


