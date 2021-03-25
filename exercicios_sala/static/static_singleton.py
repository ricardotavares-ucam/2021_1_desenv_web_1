class Livro:

    __lista_livros = None

    @staticmethod
    def get_lista_livros():
        if Livro.__lista_livros is None:
            Livro.__lista_livros = []
        return Livro.__lista_livros

    def __init__(self, titulo, autor, tipo_livro, qtde=1):
        self._titulo = titulo
        self._autor = autor
        self._qtde = qtde

    def set_titulo(self, novo_titulo):
        self._titulo = novo_titulo

    def get_titulo(self):
        return self._titulo

    def acrescenta_qtde(self):
        self._qtde += 1


livro_1 = Livro('Python Intro', 'Ricardo Tavares', 'CAPA DURA')
livro_2 = Livro('The Art of War', 'Sun Tzu', 'LIVRO NORMAL')
livro_3 = Livro('A Arte da Guerra', 'Sun Tzu', 'EBOOK')

lista_livros = Livro.get_lista_livros()
lista_livros.append(livro_1)
lista_livros.append(livro_2)
lista_livros.append(livro_3)

print(lista_livros)

for numero, livro in enumerate(lista_livros):
    print(numero, end="\t")
    print(livro.get_titulo())
