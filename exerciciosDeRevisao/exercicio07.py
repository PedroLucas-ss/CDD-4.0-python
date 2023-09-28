base = float(input("Qual o valor da base? "))
while base <= 0:
    base = float(input("Por favor digite um valor valido: "))

altura = float(input("Qual a altura? "))
while altura <= 0:
    base = float(input("Por favor digite um valor valido: "))

area = (base * altura) / 2
print(f"a area do triangulo e {area}")
