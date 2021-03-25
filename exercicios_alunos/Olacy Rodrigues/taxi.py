from datetime import datetime
from time import ctime

def cadastrar_Cliente():
    codigo_Cliente = int(input("entre com o código do cliente:"))
    nome_Cliente   = input("entre com o nome do cliente: ")
    return nome_Cliente, codigo_Cliente

def iniciar_corrida():
    dataHora_atual = datetime.now() 
    dataHora_inicio_corrida = dataHora_atual.strftime("Data: %d/%m/%Y  Hora: %H:%M")
    hora_inicio_corrida = (ctime().split()[3])
    return dataHora_inicio_corrida, hora_inicio_corrida

def finalizar_corrida():
    dataHora_atual = datetime.now()
    dataHora_fim_corrida = dataHora_atual.strftime("Data: %d/%m/%Y  Hora: %H:%M")
    hora_fim_corrida = (ctime().split()[3])
    return dataHora_fim_corrida, hora_fim_corrida

def calcular_tempo_corrida(dataHora_inicio_corrida,dataHora_fim_corrida):
    tempo_total_corrida = (dataHora_fim_corrida - dataHora_inicio_corrida)
    return tempo_total_corrida

def calcular_sobretaxa(hora_inicio_corrida,hora_fim_corrida,tempo_total_corrida):
    valor_inicial_corrida = 5.50
    valor_corrida_minuto = 0.75
    sobretaxa = 0.15
    if((hora_inicio_corrida> 22 ) and (hora_fim_corrida < 6)):
        valor_corrida = (valor_inicial_corrida +(tempo_total_corrida * valor_corrida_minuto)) * sobretaxa
    else:
        valor_corrida = (valor_inicial_corrida +(tempo_total_corrida * valor_corrida_minuto))
    return valor_corrida

def extrato_topo(informacoes_corrida):
    print("============================================")
    print("-------------Extrato da Corrida-------------")
    print("============================================")
    print("código do cliente: {}".format(informacoes_corrida["codigo_Cliente"]))
    print("Nome do cliente: {}".format(informacoes_corrida["nome_Cliente"]))
    print(datetime.now().strftime("Fatura emetida em Data: %d/%m/%Y  Hora: %H:%M"))
    print("============================================")

def extrato_informacoes_corrida(informacoes_corrida):
    print("Início da corrida: {}".format(informacoes_corrida["dataHora_inicio_corrida"]))
    print("Fim da corrida: {}".format(informacoes_corrida["dataHora_fim_corrida"]))
    print("Duração da corrida: {}".format(informacoes_corrida["tempo_total_corrida"]))
    print("Valor da corrida: {:2.f}".format(informacoes_corrida[valor_corrida]))

def imprimir_extrato(informacoes_corrida):
    extrato_topo(informacoes_corrida)
    extrato_informacoes_corrida(informacoes_corrida)


