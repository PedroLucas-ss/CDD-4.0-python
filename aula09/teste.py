import os

jogadorUm = input("Jogador 1, digite seu nome: ")
jogadorDois = input("Jogador 2, digite seu nome: ")
os.system('cls')
escolhaJogadorUm = input(f'{jogadorUm} faca sua escolha: T para tesoura, P para papel e R para pedra: ')
os.system('cls')
escolhaJogadorDois = input(f'{jogadorDois} faca sua escolha: T para tesoura, P para papel e R para pedra: ')
os.system('cls')
if (escolhaJogadorUm == escolhaJogadorDois):
    print('EMPATE')
elif ((escolhaJogadorUm == 'T' and  escolhaJogadorDois == 'P') or (escolhaJogadorUm == 'P' and escolhaJogadorDois == 'R') or
      (escolhaJogadorUm == 'R' and escolhaJogadorDois == 'T')):
    print(f"{jogadorUm} foi o ganhador")
else:
    print(f"{jogadorDois} foi o ganhador")



