from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, *args):
        self._codigo = args[0]
        self._codigo_cliente = args[1]
        self._codigo_livro = args[2]
        self._data_emprestimo = datetime.now()
        delta_tempo = timedelta(days=7)
        self._data_devolucao_prevista = self._data_emprestimo + delta_tempo
        self._data_devolucao_real = None
    
    def get_codigo(self):
        return self._codigo
    
    def get_codigo_cliente(self):
        return self._codigo_cliente
    
    def get_codigo_livro(self):
        return self._codigo_livro

    def get_data_emprestimo(self):
        return self._data_emprestimo
    
    def get_data_devolucao_prevista(self):
        return self._data_devolucao_prevista
    
    def set_data_devolucao_real(self, data_devolucao_real):
        self._data_devolucao_real = data_devolucao_real
    
    def get_data_devolucao_real(self):
        self._data_devolucao_real
    
    
    
