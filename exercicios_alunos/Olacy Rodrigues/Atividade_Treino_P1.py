#1) Desenvolva um código utilizando a linguagem de programação Python para:
#• Construir uma classe para executar cálculos de distância entre pontos.
#• Atributos: dicionário com indicação de pontos cartesianos
#• Métodos: apensar pontos a uma lista; executar cálculo da distância euclidiana e de manhattan;


#=====fazer dps=====

#______________________________________________________________________________________________________________
#2) Desenvolva um código utilizando a linguagem de programação Python para:
#• Calcular a probabilidade de acidentes de trânsito.
#• Usuário irá entrar com a causa de um acidente e o meio de transporte e
#seu software deverá retornar à probabilidade daquele evento ocorrer dados_acidentes = 
# { 'causa' : ['Ingestão de álcool', 'Desobediência à sinalização', 'Defeito na via', 'Falta de atenção', 'Outras'],
# 'a pé' : [3, 1, 1, 9, 6],
# 'bicicleta' : [1, 0, 0, 0, 1],
# 'carro' : [17, 9, 7, 9, 6],
# }

#=====fazer dps=====


#______________________________________________________________________________________________________________
#3) O que são métodos de uma classe ou funções? Para que servem? Quais são seus objetivos principais?

print("Um método é um trecho de código que realiza uma função específica e pode ser chamado por qualquer outro\
    método ou classe para realizar a referida função num determinado contexto.")

#______________________________________________________________________________________________________________

#4) Um nutricionista necessita de um software para controlar os cadastros de
#seus clientes, suas consultas, as medidas de peso e IMC e as dietas receitadas a cada visita.
#Os dados coletados durante a entrevista com o nutricionista foram:
#Os cadastros dos clientes devem conter: nome, telefone, CPF, peso inicial, IMC inicial;
#Os cadastros das dietas devem conter: o tipo de refeição, os alimentos e quantidades
#As consultas devem conter: data e hora, cliente atendido, a receita da dieta, peso
#medido na visita, IMC calculado no momento da visita, a data da próxima visita.

class Cliente:
    def __init__(self,**kwargs):
        self._nome = kwargs ["nome"]
        self._telefone = kwargs ["telefone"]
        self._cpf = kwargs ["cpf"]
        self._peso_inicial = kwargs ["peso_inicial"]
        self._IMC_inicial = kwargs ["IMC_inicial"]

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self,telefone):
        self._telefone = telefone

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self,cpf):
        self._cpf = cpf

    @property
    def peso_inicial(self):
        return self._peso_inicial

    @peso_inicial.setter
    def peso_inicial(self,peso_inicial):
        self._peso_inicial = peso_inicial

    @property
    def IMC_inicial(self):
        return self._IMC_inicial

    @IMC_inicial.setter
    def IMC_inicial(self,IMC_inicial):
        self._IMC_inicial = IMC_inicial

class dieta:
    def __init__(self, **kwargs):
        self._tipo_refeicao = kwargs ["tipo_refeicao"]
        self._alimentos = kwargs ["alimentos"]
        self._quantidades = kwargs ["quantidades"]

    @property
    def tipo_refeicao(self):
        return self._tipo_refeicao

    @tipo_refeicao.setter
    def tipo_refeicao(self,tipo_refeicao):
        self._tipo_refeicao = tipo_refeicao

    @property
    def alimentos(self):
        return self._alimentos

    @alimentos.setter
    def alimentos(self,alimentos):
        self._alimentos = alimentos

    @property
    def quantidades(self):
        return self._quantidades

    @quantidades.setter
    def quantidades(self,quantidades):
        self._quantidades = quantidades

from datetime import datetime

class consulta:
    def __init__(self, **kwargs):
        self._data_hora_consulta = kwargs ["data_hora_consulta"]
        self._cliente = kwargs ["cliente"]
        self._receita_dieta = kwargs ["receita_dieta"]
        self._peso_visita = kwargs ["peso_visita"]
        self._IMC_visita = kwargs ["IMC_visita"]
        self._data_prox_visita = kwargs ["data_prox_visita"]

    def data_hora_consulta(self):
        self._data_hora_consulta = datetime.now()

    @property
    def Cliente(self):
        return self._cliente

    @property
    def dieta(self):
        return self._receita_dieta

    @property
    def peso_visita(self):
        return self._peso_visita

    @peso_visita.setter
    def peso_visita(self,peso_visita):
        self._peso_visita = peso_visita

    @property
    def IMC_visita(self):
        return self._IMC_visita

    @IMC_visita.setter
    def IMC_visita(self,IMC_visita):
        self._IMC_visita = IMC_visita

    @property
    def data_prox_visita(self):
        return self._data_prox_visita

    @data_prox_visita.setter
    def data_prox_visita(self,data_prox_visita):
        self._data_prox_visita = data_prox_visita


