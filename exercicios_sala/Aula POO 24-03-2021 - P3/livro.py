class Livro:
    def __init__(self, *args):
        self._codigo = args[0]
        self._nome = args[1]
        self._autor = args[2]
        self._edicao = args[3]
        self._isbn = args[4]
        self._quantidade = 1
    
    def get_codigo(self):
        return self._codigo

    def get_nome(self):
        return self._nome

    def get_autor(self):
        return self._autor
    
    def get_edicao(self):
        return self._edicao
    
    def get_isbn(self):
        return self._isbn
    
    def aumentar_quantidade(self):
        self._quantidade += 1
    
    def get_quantidade(self):
        return self._quantidade