class Pessoa:
    def __init__(self, *args):
        self._id = args[0]
        self._nome = args[1]
        self._endereco = args[2]

    def get_nome(self):
        return self._nome


class PessoaFisica(Pessoa):
    def __init__(self, *args):
        super().__init__(*args)
        self._cpf = args[3]


class PessoaJuridica(Pessoa):
    def __init__(self, *args):
        super().__init__(*args)
        self._cnpj = args[3]


pf1 = PessoaFisica(1, 'Ricardo Tavares', '09252571760', 'UCAM')
pj1 = PessoaJuridica(1, 'UCAM-Campos', '123456789', 'Campos dos Goytacazes')

print(pf1.get_nome())
print(pj1.get_nome())
