nomes = ["","","","",""]
senhas = [0,0,0,0,0]
y= 3
j = 3
for i in range(2):
    nomes[i] = input("Digite seu nome: ")
    senhas[i] = int(input("Digite sua senha: "))

nome = input("Digite o seu nome para efetuar o login do sistema: ")
if nome in nomes:
    for x in range(2):
        if nome == nomes[x]:
            senha = int(input("Digite sua senha: "))
            if senha == senhas[x]:
                print(f"{nome}, {senha}, {x}")
            else:
                while y > 0:
                    senha = int(input(f"Senha incorreta, por favor tente novamente(voce tem {y} tentativas): "))
                    if senha == senhas[x]:
                        print(f"{nome}, {senha}, {x}")
                        break
                    y-=1
            if y == 0:
                trocarSenha = input("Deseja trocar a senha?(s/n)")
                if trocarSenha == "s":
                    senhas[x] = int(input("Digite sua nova senha: "))
                    print("Senha cadastrada com sucesso")
else:
    for l in range(2):
        nome = input("usuario invalido, por favor tente novamente: ")
        if nome == nomes:
            break


