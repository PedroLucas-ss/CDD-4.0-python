class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O animal {self.nome} foi comer")
    def som(self):
        print(f"O {self.nome} faz um som")
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def som(self):
        print(f"o {self.nome} mia")
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def som(self):
        print(f"O {self.nome} late")
class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def som(self):
        print(f"A {self.nome} mugi")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def som(self):
        print(f"O {self.nome} faz alguma coisa")


gato = Gato("pedro", "laranja")
vaca = Vaca("joao", "preta")
cachorro = Cachorro("lucas", "marrom")
coelho = Coelho("sla", "branco")

gato.som()
vaca.som()
cachorro.som()
coelho.som()



