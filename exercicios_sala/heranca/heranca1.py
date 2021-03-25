class PessoaFisica:
    def __init__(self, *args):
        self._id = args[0]
        self._nome = args[1]
        self._cpf = args[2]
        self._endereco = args[3]

    def get_nome(self):
        return self._nome


class PessoaJuridica:
    def __init__(self, *args):
        self._id = args[0]
        self._nome = args[1]
        self._cnpj = args[2]
        self._endereco = args[3]

    def get_nome(self):
        return self._nome


pf1 = PessoaFisica(1, 'Ricardo Tavares', '09252571760', 'UCAM')
pj1 = PessoaJuridica(1, 'UCAM-Campos', '123456789', 'Campos dos Goytacazes')

print(pf1.get_nome())
print(pj1.get_nome())
