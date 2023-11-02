class ContaBancaria:

    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.saldo = 0
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = 0
        self.limiteRestante = 0

    def depositar(self, deposito):
        if self.status == True:
            if deposito > 0:
                if self.limite != self.limiteRestante:
                    if self.limiteRestante+ deposito> self.limite:
                        self.saldo=  (self.limiteRestante + deposito) - self.limite
                        print(f"usamos {self.limite- self.limiteRestante} do seu deposito para restaurar seu limite, seu saldo e de {self.saldo}")
                    else:
                        self.limiteRestante += deposito
                        print(f"usamos o valor depositado para quitar seu limite, Limite atual e de {self.limiteRestante}")
                else:
                    self.saldo += deposito
                    print(f"Seu saldo foi atualizado para {self.saldo}")

            else:
                print(f"valor de deposito invalido")
        else:
            print(f"Sua conta ainda nao esta ativa")

    def sacar(self, valorDeSaque):
        if self.status == True:
            if self.saldo > valorDeSaque and valorDeSaque >0 :
                print(f"Sr(a) {self.nome} seu saque de R$ {valorDeSaque} foi efetuado com sucesso")
            elif valorDeSaque > self.saldo and self.limite != 0 and valorDeSaque >0:
                self.limiteRestante -=  valorDeSaque - self.saldo
                print(f"Sr(a) {self.nome} voce usou seu credito para efetuar esse saque, agora seu limite e de {self.limiteRestante}")
                self.saldo = 0
            else:
                print("esse valor nao pode ser sacado")
        else:
            print(f"Sua conta ainda nao esta ativa")

    def ativarConta(self):
        if self.status ==  False:
            print(f"sua conta foi ativa")
            self.status = True
        else:
            print("sua conta ja esta ativa")

    def verificarSaldo(self):
        if self.status == True:
            print(f"{self.nome} o seu saldo e de R$ {self.saldo}")
        else:
            print(f"Sua conta ainda nao esta ativa")

    def habilitarLimite(self, limite):
        if self.status == True:
            if limite < 0:
                print("valor de limite invalido.")
            else:
                self.limite = limite
                self.limiteRestante = limite

                print("credito contradado")
        else:
            print(f"Sua conta ainda nao esta ativa")
