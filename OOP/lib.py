class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.dormindo = False
        self.falando = False

    def falar(self):
        if self.comendo:
            print(f"{self.nome} esta comendo, nao pode falar agora")
        elif self.dormindo:
            print(f"{self.nome} esta dormindo, nao pode falar agora")
        elif self.falando:
            print(f"{self.nome} ja esta falando")
        else:
            self.falando = True
            print(f"{self.nome} esta falando")
    def comer(self, comida):
        if self.dormindo:
            print(f"{self.nome} esta dormindo, nao pode comer agora")
        elif self.falando:
            print(f"{self.nome} esta falando, nao pode comer agora")
        elif self.comendo:
            print(f"{self.nome} ja esta comendo {comida}")
        else:
            self.comendo = True
            print(f"{self.nome} esta comendo {comida}")
    def dormir(self):

        if self.comendo:
            print(f"{self.nome} esta comendo, nao pode dormir agora")
        elif self.falando:
            print(f"{self.nome} esta falando, nao pode dormir agora")
        elif self.dormindo:
            print(f"{self.nome} ja esta dormindo")
        else:
            self.dormindo = True
            print(f"{self.nome} esta dormindo")

    def pararDeComer(self):
        if self.comendo:
            print(f"{self.nome} parou de comer ")
            self.comendo = False
        else:
            print(f"{self.nome} vc nao esta comendo, nao tem oq parar")
    def pararDeFalar(self):
        if self.falando:
            print(f"{self.nome} parou de falar ")
            self.falando = False
        else:
            print(f"{self.nome} vc nao estava falando, nao tem oq parar")
    def pararDeDormir(self):
        if self.dormindo:
            print(f"{self.nome} acordou")
            self.dormindo =  False
        else:
            print(f"{self.nome} vc nao estava dormindo, nao tem oq parar")





    def apresentar(self):
        print(f"Boa tarde meu nome e {self.nome} tenho {self.idade} anos e peso {self.peso} kilos")




