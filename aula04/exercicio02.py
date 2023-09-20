quandidadeDeNumero = int(input("Digite quantos numeros voce quer tirar a media: "))
somaValores = 0
for i in range(quandidadeDeNumero):
    valores = float(input("Digite um numero: "))
    somaValores += valores
media = somaValores/quandidadeDeNumero
print(f'media: {media}')