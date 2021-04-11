# classe gerenciadora
# será a responsável por enviar/solicitar ações das outras classes

from cliente import Cliente
from emprestimo import Emprestimo
from livro import Livro

class Biblioteca:
    
    def __init__(self):
        self._lista_clientes = []
        self._lista_livros = []
        self._lista_emprestimos = []
    
    def cadastrar_cliente(self, *args):
        cliente = Cliente(*args)
        self._lista_clientes.append(cliente)
    
    def cadastrar_livro(self, *args):
        livro = Livro(*args)
        self._lista_livros.append(livro)
    
    def is_quantidade_emprestimo_maximo(self, codigo_cliente):
        count = 0
        if len(self._lista_emprestimos) > 0:
            for emprestimo in self._lista_emprestimos:
                if emprestimo.get_codigo_cliente() == codigo_cliente:
                    count += 1
            if count < 2:
                return False
            else:
                return True
        else:
            print('Não existem empréstimos cadastrados')
        
    def registrar_emprestimo(self, codigo_cliente, *args):
        if self.is_quantidade_emprestimo_maximo(codigo_cliente):
            print('Cliente já possui dois empréstimos')
        else:
            emprestimo = Emprestimo(*args)
            self._lista_emprestimos.append(emprestimo)
    
    def imprimir_relatorio_clientes_cadastrados(self):
        for cliente in self._lista_clientes:
            print(cliente.get_codigo(), cliente.get_nome())
    
    def imprimir_relatorio_livros_cadastrados(self):
        for livro in self._lista_livros:
            print(livro.get_codigo(), livro.get_nome())
    
    def imprimir_relatorio_emprestimos(self):
        for emprestimo in self._lista_emprestimos:
            print(emprestimo.get_codigo_cliente(), end = '\t')
            print(emprestimo.get_codigo_livro(), end = '\t')
            print(emprestimo.get_data_emprestimo(), end = '\t')
            print(emprestimo.get_data_devolucao_prevista(), end = '\t')
            print(emprestimo.get_data_devolucao_real())