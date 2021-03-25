class Livro:

    def __init__(self, titulo, autor, isbn, valor):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        # TODO: inserir valor
        self._valor = valor

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_isbn(self):
        return self._isbn

    def get_valor(self):
        if hasattr(self, '_desconto'):
            return self._valor - (self._valor * self._desconto)
        else:
            return self._valor

    def set_desconto(self, desconto):
        self._desconto = desconto


class Cliente:

    def __init__(self, id, nome, endereco):
        self._id = id
        self._nome = nome
        self._endereco = endereco


livro_1 = Livro('Python Intro', 'Ricardo Tavares', '123456', 25.00)
livro_2 = Livro('A Arte da Guerra', 'Sun Tzu', '987654', 35.00)
cliente_1 = Cliente(1, 'Uchiha Sasuke', 'Vila da Folha')
cliente_2 = Cliente(2, 'Uzumaki Naruto', 'Vila da Folha')

# TODO: isinstance e type

print(type(livro_1))
print(type(cliente_1))

print(type(livro_1) == type(livro_2))
print(type(cliente_1) == type(cliente_2))
print(type(livro_1) == type(cliente_2))

print(isinstance(livro_1, Livro))
print(isinstance(cliente_1, Cliente))
print(isinstance(cliente_2, Livro))
print(isinstance(cliente_2, object))
print(isinstance(livro_1, object))
