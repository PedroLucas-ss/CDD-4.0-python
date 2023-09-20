numeroUm = float(input('Digite um numero: '))
numeroDois =float(input('Digite o segundo  numero: '))
errado = 1
while numeroDois == 0 and errado  != 5:
    numeroDois = float(input('Digite um numero diferente de 0: '))
    errado += 1
if numeroDois != 0:
 print(numeroUm/numeroDois)
else:
    print('vc cometeu muitos erros')
    print('Execução terminada')








