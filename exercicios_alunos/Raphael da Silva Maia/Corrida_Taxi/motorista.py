class motorista:
    def __init__(self nome, senha, tipo_Habilitacao):
        self.nome = nome
        self.senha = senha
        self.tipo_habilitacao = tipo_Habilitacao
    def getNome(self):
        return self.nome
    def getTipo_Habilitacao(self):
        return self.tipo_Habilitacao