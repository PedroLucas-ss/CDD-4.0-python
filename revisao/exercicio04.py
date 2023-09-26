numUm = int(input("Digite o numero um"))
numDois = int(input("Digite o numero dois"))
numTres = int(input("Digite o numero tres"))

if numUm < numDois > numTres:
    print(numDois)
elif numDois < numTres > numUm:
    print(numTres)
else:
    print(numUm)