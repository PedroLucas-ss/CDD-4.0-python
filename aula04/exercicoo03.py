
negativo = 0
somaNegativo = 0
for i in range (10):

  num =  int(input("digite um numero: "))

  if num < 0:
      negativo +=1
      print(num)
      somaNegativo = somaNegativo + num

#print(negativo, ' numeros são negativos')

print((i +1) - negativo)
#print('A soma dessews numeros é: ', somaNegativo)