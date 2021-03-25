class Livro:

    def __init__(self, titulo, autor, codigo, valor):
        self._titulo = titulo
        self._autor = autor
        self._codigo = codigo
        # TODO: inserir valor
        self._valor = valor

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_isbn(self):
        return self._codigo

    # TODO: método valor e desconto
    def get_valor(self):
        if hasattr(self, '_desconto'):
            return self._valor - (self._valor * self._desconto)
        else:
            return self._valor

    def set_desconto(self, desconto):
        self._desconto = desconto


# TODO: passar outros argumentos
livro_1 = Livro('Python Intro', 'Ricardo Tavares', '123456', 25.00)
livro_2 = Livro('A Arte da Guerra', 'Sun Tzu', '987654', 35.00)

print(livro_1.get_titulo(), livro_1.get_valor())
livro_1.set_desconto(0.25)
print(livro_1.get_titulo(), livro_1.get_valor())
