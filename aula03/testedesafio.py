entradaHoraUm = int(input("digite a primeira hora: ", ))
entradaMinutoUm = int(input("digite os minutos da primeira hora: ", ))
entradaHoraDois = int(input("digite a segunda hora: ", ))
entradaMinutoDois = int(input("digite os minutos da segunda hora: ", ))

saidaMinuto = entradaMinutoUm + entradaMinutoDois

saidaHora = 0



if saidaMinuto >=60:
     saidaMinuto -= 60
     saidaHora += 1


if entradaHoraUm >= 12:
     entradaHoraUm -= 12

if entradaHoraDois >= 12:
     entradaHoraDois -= 12

somaTotal = entradaHoraUm + entradaHoraDois + saidaHora

if somaTotal >= 12:
     somaTotal -= 12


print(somaTotal, ":",saidaMinuto)

