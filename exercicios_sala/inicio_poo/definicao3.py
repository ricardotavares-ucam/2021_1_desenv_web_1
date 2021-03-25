class Livro:

    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        # TODO: inserir mais propriedades
        self._autor = autor
        self._isbn = isbn

    # TODO: criar métodos para trabalhar com a classe
    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_isbn(self):
        return self._isbn


# TODO: passar outros argumentos
livro_1 = Livro('Python Intro', 'Ricardo Tavares', '123456')
livro_2 = Livro('A Arte da Guerra', 'Sun Tzu', '987654')

# TODO: imprimir argumentos
print(livro_1)
print(livro_1._titulo)  # isso é errado!!! Com grandes poderes vem grandes responsabilidades!!! By: Uncle Ben!

print(livro_1.get_titulo(), livro_1.get_autor(), livro_1.get_isbn())  # Uncle Ben Smile!! :D
print(livro_2.get_titulo(), livro_2.get_autor(), livro_2.get_isbn())  # Uncle Ben Smile!! :D
