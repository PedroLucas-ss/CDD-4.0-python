idadeAno = int(input("quantos anos vc tem? "))
mes = int(input("qual o mes do seu nascimento? "))
dia = int(input("em que dia vc nasceu"))

totalDias = (idadeAno*365)+(mes*30)+ (30-dia)
print(totalDias)