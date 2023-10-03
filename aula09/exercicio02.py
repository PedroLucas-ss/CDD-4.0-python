nomes = ["","","","",""]
senhas = [0,0,0,0,0]
x= 3
for i in range(2):
    nomes[i] = input("Digite seu nome: ")
    senhas[i] = int(input("Digite sua senha: "))

nome = input("digite seu nome: ")
if nome in nomes:
    senha = int(input("Digite sua senha: "))
    if senha in senhas:
        print(f"Login bem Sucedido: Usuario: {nome} | Senha: {senha}")
    else:
        while x > 0:
            senha = int(input(f"Senha incorreta, por favor tente novamente(voce tem {x} tentativas): "))
            if senha in senhas:
                print(f"Login bem Sucedido: Usuario: {nome} | Senha: {senha}")
                break
            x = x-1
        mudarSenha= input("voce exedeu o numero maximo de tentativas, deseja cadastrar uma nova senha?(s/n) ")
        if mudarSenha == "s":
            print()

else:
    while True:
        nome = input("Usuario invalido, por favor tente novamente: ")
        if nome in nomes:
            break

