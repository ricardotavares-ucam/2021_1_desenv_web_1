# Criação de uma classe básica:


# pode se usar também class Livro():
# mas só é obrigatório no caso de herança de outra classe
class Livro:

    # quando um objeto é instanciado a função __init__
    # é a primeira função a ser chamada.
    # ela é responsável por inicializar o objeto
    # com informações passadas ou setadas internamente
    # self: toda a vez que chamamos um método em um objeto python
    # é necessário passar o objeto em si no método, isso é feito
    # automaticamente e sempre sendo o primeiro argumento do método
    # não é obrigatório ser self, pode ser outro nome, mas é convenção PEP8
    def __init__(self, titulo):
        self._titulo = titulo


# TODO: criar 2 instancias do classe livro
livro_1 = Livro('Python Intro')
livro_2 = Livro('A Arte da Guerra')

# TODO: imprimir a classe e a propriedade
print(livro_1)
print(livro_1._titulo)
print(livro_2)
print(livro_2._titulo)
