votosValidos = int(input("Digite q quantidade de votos validados: "))
votosBrancos = int(input("Digite q quantidade de votos brancos: "))
votosNulos = int(input("Digite q quantidade de votos nulos: "))
totalVotos = votosNulos + votosBrancos + votosValidos



percentVali = (votosValidos / totalVotos) *100
percentBr = (votosBrancos/totalVotos ) *100
precentNul = (votosNulos/totalVotos) *100


print(f'Total de votos: {totalVotos} \n votos validos: {percentVali:.2f}% \n votos brancos: {percentBr:.2f}% \n votos nulos{precentNul:.2f}%')