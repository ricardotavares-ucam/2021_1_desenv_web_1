from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, *args):
        super().__init__()
        self._codigo = args[0]
        self._nome = args[1]
        self._saldo = args[2]

    @abstractmethod
    def realiza_deposito(self, valor):
        self._saldo += valor

    @abstractmethod
    def verifica_saldo(self):
        return self._saldo

    @abstractmethod
    def realiza_saque(self, valor):
        self._saldo -= valor
