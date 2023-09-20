contadorDentro = 0

for i in range(10):
    numero = int(input("DIgite um numero: "))

    if numero >= 10 and numero<=20:
        contadorDentro += 1

contadorFora = 10 - contadorDentro

print(f"{contadorDentro} numero estao dentro do intervalo")
print(f"{contadorFora} numero estao fora do intervalo")




