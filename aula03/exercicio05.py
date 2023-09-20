soma = 0
for i in range(10):
    numero = int(input("Digite um numero"))
    if numero %2 != 0:
         soma += numero
print(soma)