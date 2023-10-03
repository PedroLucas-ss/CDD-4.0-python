valor = int(input("Digite um numero"))
vetorA= [0]*valor
vetorB= [0]*valor
vetorC= [0]*valor
for i in range(valor):
    vetorA[i] = int(input(f"digite o {i+1}° valor de A "))
    vetorB[i] = int(input(f"digite o {i+1}° valor de B "))
    vetorC[i] = vetorA[i]+vetorB[i]
print(vetorA)
print('+')
print(vetorB)
print('=')
print(vetorC)

