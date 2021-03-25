class Conta:
    def __init__(self, numero, saldo=0):
        self._saldo = saldo
        self._numero = numero
    
    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, saldo):
        if(saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo

c1 = Conta(1, 50)
# print(c1.get_saldo())

print(c1._saldo)