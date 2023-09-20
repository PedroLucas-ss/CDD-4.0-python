time1 = input("Qual o nome do seu time: ")
golsTime1 = int(input("Quantos gols o " + time1 + ' marcou? '))
time2 = input("Qual o nome do seu time: ")
golsTime2 = int(input("Quantos gols o " + time2 + ' marcou? '))


if golsTime1 != golsTime2:
   if golsTime1 > golsTime2:
     print("o ", time1, "venceu")
   else:
       print("o ", time2, "venceu")
else:
    print("EMPATE")


