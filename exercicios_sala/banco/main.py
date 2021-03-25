from conta_pessoa_fisica import PessoaFisica
from conta_pessoa_juridica import PessoaJuridica

if __name__ == "__main__":
    cliente1 = PessoaFisica('123456789', '321', 'Ricardo', 0)
    cliente1.realiza_deposito(100)
    print(cliente1.verifica_saldo())
    cliente1.realiza_saque(50)
    print(cliente1.verifica_saldo())

    clientePJ1 = PessoaJuridica('987654321', 'Alpha1', 'UCAM', 0)
    clientePJ1.realiza_deposito(1000000)
    print(clientePJ1.verifica_saldo())
    clientePJ1.realiza_saque(5000)
    print(clientePJ1.verifica_saldo())
