from conta import Conta


class PessoaJuridica(Conta):
    def __init__(self, cnpj, *args):
        super().__init__(*args)
        self._cnpj = cnpj

    def realiza_deposito(self, valor):
        self._saldo += valor

    def verifica_saldo(self):
        return self._saldo

    def realiza_saque(self, valor):
        self._saldo -= valor
