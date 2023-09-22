vetorNum= [0,0,0,0,0,0,0,0,0,0]
vetorMulti= [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    numero = float(input("Digite um numero: "))
    vetorNum[i] = numero

multi =  int(input("Digite o numero para efetuar a multiplicacao: "))

for x in range(10):
    vetorMulti[x] = vetorNum[x]*multi
print(vetorMulti)