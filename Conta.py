class Conta:

    def __init__(self,numero,titular,saldo,limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def limite (self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    def deposita(self,valor):
        self.__saldo += valor

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return (valor_a_sacar <= valor_disponivel_a_sacar)


    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite!".format(self.__valor))

    def transfere(self,valor,destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @staticmethod
    def codigos_bancos():
        return {'BB':'001','Caixa':'104','Bradesco':'237'}

    def extrato(self):
        print("Titular: {}\nNumero: {}\nSaldo: {}\nLimite: {}".format(self.__titular,self.__numero,self.__saldo,self.__limite) )



conta = Conta(366,"Matheus",5000.0,1000.0)
conta.saca(6000.0)
conta.extrato()
