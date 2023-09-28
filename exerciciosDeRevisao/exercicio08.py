soma = 0
quantRepet = int(input("Quantos numeros vc deseja calcular?"))
for i in range(quantRepet):
    numero = float(input("DIgite um numero: "))
    soma = soma + numero
media = soma /quantRepet
print(f"media = {media} soma = {soma}")
