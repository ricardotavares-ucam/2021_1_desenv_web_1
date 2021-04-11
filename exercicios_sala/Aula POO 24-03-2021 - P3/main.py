from biblioteca import Biblioteca

def main():
    biblioteca_1 = Biblioteca()
    biblioteca_1.cadastrar_cliente(1, 'Anakin Skywalker', '1234', 'Rua xxxxxx', '987654321')
    biblioteca_1.cadastrar_cliente(2, 'Luke Skywalker', '2345', 'Rua yyyyyy', '999999999')
    biblioteca_1.imprimir_relatorio_clientes_cadastrados()
    biblioteca_1.cadastrar_livro(1, 'Python Intro', 'Guido van Rossum', '1a edição', '78901')
    biblioteca_1.cadastrar_livro(2, 'Python Intermediário', 'Guido van Rossum', '1a edição', '78912')
    biblioteca_1.cadastrar_livro(3, 'Python Avançado', 'Guido van Rossum', '2a edição', '78923')
    biblioteca_1.imprimir_relatorio_livros_cadastrados()
    #1ª posicao:cod_cliente 
    #2ª posicao:cod_emprestimo
    #3ª posicao:cod_cliente 
    #4ª posicao:cod_livro
    biblioteca_1.registrar_emprestimo(1, 1, 1, 1)
    biblioteca_1.registrar_emprestimo(1, 2, 1, 2)
    biblioteca_1.registrar_emprestimo(1, 3, 1, 3)
    biblioteca_1.imprimir_relatorio_emprestimos()


if __name__ == "__main__":
    main()