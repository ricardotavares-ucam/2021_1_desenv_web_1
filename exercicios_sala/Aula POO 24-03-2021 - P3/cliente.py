class Cliente:
    def __init__(self, *args):
        self._codigo = args[0]
        self._nome = args[1]
        self._matricula = args[2]
        self._endereco = args[3]
        self._telefone = args[4]
    
    def get_codigo(self):
        return self._codigo

    def get_nome(self):
        return self._nome

    def get_matricula(self):
        return self._matricula
    
    def get_endereco(self):
        return self._endereco
    
    def get_telefone(self):
        return self._telefone
