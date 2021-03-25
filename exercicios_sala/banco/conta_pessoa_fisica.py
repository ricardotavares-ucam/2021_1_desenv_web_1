from conta import Conta


class PessoaFisica(Conta):
    def __init__(self, cpf=0, *args):
        super().__init__(*args)
        self._cpf = cpf

    def realiza_deposito(self, valor):
        self._saldo += valor

    def verifica_saldo(self):
        return self._saldo

    def realiza_saque(self, valor):
        self._saldo -= valor
