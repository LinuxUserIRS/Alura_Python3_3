class Conta:
    def __init__(self, num, name, balance, limit=1000):
        print("Construindo objeto...{}".format(self))
        self.num = num
        self.name = name
        self.balance = balance
        self.limit = limit

    def extrato(self):
        return self.balance

    def deposita(self, num):
        self.balance += num

    def saca(self, num):
        if self.balance-num > 0:
            self.balance -= num
        else:
            print("Você não tem saldo suficiente")