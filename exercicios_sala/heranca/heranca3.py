class Livro:
    def __init__(self, titulo, autor, paginas, preco):
        self._titulo = titulo
        self._autor = autor
        self._paginas = paginas
        self._preco = preco


class Revista:
    def __init__(self, titulo, editora, preco, periodo):
        self._titulo = titulo
        self._editora = editora
        self._preco = preco
        self._periodo = periodo


class Jornal:
    def __init__(self, titulo, editora, preco, periodo):
        self._titulo = titulo
        self._editora = editora
        self._preco = preco
        self._periodo = periodo


livro_1 = Livro('Python Intro', 'Ricardo Tavares', 200, 29.90)
revista_1 = Revista('Revista Python', 'TI Tec', 10.90, 'mar-2020')
jornal_1 = Jornal('NY Times', 'NY Times Editora', 3.90, '12-09-2020')

print(livro_1._titulo)
print(revista_1._titulo)
print(jornal_1._titulo)
print(livro_1._preco, revista_1._preco, jornal_1._preco)
