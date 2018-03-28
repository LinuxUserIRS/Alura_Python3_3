class Conta:
    #Função __init__ é o construtor da classe
    #Parâmetro limite é padrão
    def __init__(self, num, name, balance, limit=1000):
        print("Construindo objeto...{}".format(self))
        #Os __ na frente dos atributos os deixam como privados
        self.__num = num
        self.__name = name
        self.__balance = balance
        self.__limit = limit

    def extrato(self):
        return self.__balance

    def deposita(self, num):
        self.__balance += num

    def saca(self, num):
        if self.__balance-num > 0:
            self.__balance -= num
        else:
            print("Você não tem saldo suficiente")

    def transfere(self, Conta, num):
        self.saca(num)
        Conta.deposita(num)