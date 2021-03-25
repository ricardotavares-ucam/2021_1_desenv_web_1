class Livro:

    # ATRIBUTO DA CLASSE
    TIPOS_LIVROS = ('CAPA DURA', 'EBOOK', 'CAPA NORMAL')

    @classmethod
    def get_tipos_livros(cls):
        return cls.TIPOS_LIVROS

    def __init__(self, titulo, autor, tipo_livro):
        self._titulo = titulo
        self._autor = autor
        if (tipo_livro not in Livro.TIPOS_LIVROS):
            raise ValueError('Tipo de livro inserido não é valido')
        else:
            self._tipo_livro = tipo_livro

    def set_titulo(self, novo_titulo):
        self._titulo = novo_titulo

    def get_titulo(self):
        return self._titulo


print('Tipos de livros autorizados: {}'.format(Livro.get_tipos_livros()))

livro_1 = Livro('Python Intro', 'Ricardo Tavares', 'CAPA DURA')
livro_2 = Livro('Python Intro', 'Ricardo Tavares', 'CAPA NORMAL')
livro_3 = Livro('A Arte da Guerra', 'Sun Tzu', 'EBOOK')

print(livro_3.get_titulo())
livro_3.set_titulo('The Art of War')
print(livro_3.get_titulo())
