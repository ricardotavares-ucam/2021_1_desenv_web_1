class Publicacao:
    def __init__(self, titulo, preco):
        self._titulo = titulo
        self._preco = preco

    def get_titulo(self):
        return self._titulo


class Periodico(Publicacao):
    def __init__(self, titulo, editora, preco, periodo):
        super().__init__(titulo, preco)
        self._editora = editora
        self._periodo = periodo


class Livro(Publicacao):
    def __init__(self, titulo, autor, paginas, preco):
        super().__init__(titulo, preco)
        self._autor = autor
        self._paginas = paginas


class Revista(Periodico):
    def __init__(self, titulo, editora, preco, periodo, data_referecia):
        super().__init__(titulo, editora, preco, periodo)
        self._data_referencia = data_referencia

class Jornal(Periodico):
    def __init__(self, titulo, editora, preco, periodo, qtde_paginas):
        super().__init__(titulo, editora, preco, periodo)
        self._qtde_paginas = qtde_paginas
    
    def get_qtde_paginas(self):
        return self._qtde_paginas
    
    def set_qtde_paginas(self, qtde_paginas):
        self._qtde_paginas = qtde_paginas


j1 = Jornal('Jornal da UCAM', 'UCAM', '0.00', 'mar-2021', 20)


livro_1 = Livro('Python Intro', 'Ricardo Tavares', 200, 29.90)
revista_1 = Revista('Revista Python', 'TI Tec', 10.90, 'mar-2020')
jornal_1 = Jornal('NY Times', 'NY Times Editora', 3.90, '12-09-2020')

print(livro_1._titulo)
print(revista_1._titulo)
print(jornal_1._titulo)
print(livro_1._preco, revista_1._preco, jornal_1._preco)

print(livro_1.get_titulo(), revista_1.get_titulo(), jornal_1.get_titulo())
