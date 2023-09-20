tipoDeCombustivel = input("Qual tipo de combustivel abastecido(Digite G para gasolina e E para etanol)? ")
litros = float(input("Quantos litros voce colocou de combustivel? "))


if tipoDeCombustivel == 'G':
    valorDeComb = litros*5.80
    print("O valor a pagar é: ", valorDeComb)
elif tipoDeCombustivel == 'E':
        valorDoComb = litros*4.90
        print("O valor a pagar é: ", valorDoComb)
else:
    print("combustivel invalido")