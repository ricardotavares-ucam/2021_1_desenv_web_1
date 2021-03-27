from datetime import datetime

def cadastrar_Cliente():
    codigo_cliente = int(input("entre com o código do cliente:"))
    nome_cliente   = input("entre com o nome do cliente: ")
    return codigo_cliente, nome_cliente

def iniciar_corrida():
    dataHora_inicio_corrida = datetime.now() 
    return dataHora_inicio_corrida

def finalizar_corrida():
    dataHora_fim_corrida = datetime.now()
    return dataHora_fim_corrida

def e_bandeira1(dataHora_inicio_corrida):
    if((dataHora_inicio_corrida.hour>22) and (dataHora_inicio_corrida.hour<6)):
        return False
    else:
        return True

def calcular_tempo_corrida(dataHora_inicio_corrida,dataHora_fim_corrida):
    tempo_total_corrida = (dataHora_fim_corrida - dataHora_inicio_corrida)
    tempo_total_corrida = int(tempo_total_corrida.seconds/60)
    return tempo_total_corrida

def calcular_valor_corrida(tempo_total_corrida):
    valor_inicial_corrida = 5.50
    valor_corrida_minuto = 0.75
    sobretaxa_bandeira_2 = 1.15
    if e_bandeira1:
        valor_corrida = (valor_inicial_corrida +(tempo_total_corrida * valor_corrida_minuto))
    else:
        valor_corrida = (valor_inicial_corrida +(tempo_total_corrida * valor_corrida_minuto)) * sobretaxa_bandeira_2
    return valor_corrida

def extrato_topo(informacoes_corrida):
    print("============================================")
    print("-------------Extrato da Corrida-------------")
    print("============================================")
    print("Código do cliente: {}".format(informacoes_corrida["codigo_cliente"]))
    print("Nome do cliente: {}".format(informacoes_corrida["nome_cliente"]))
    print(datetime.now().strftime("Fatura emetida em Data: %d/%m/%Y  Hora: %H:%M"))
    print("============================================")

def extrato_informacoes_corrida(informacoes_corrida):
    print("Início da corrida: {}".format(informacoes_corrida["dataHora_inicio_corrida"].strftime("%d/%m/%Y - %H:%M")))
    print("Fim da corrida: {}".format(informacoes_corrida["dataHora_fim_corrida"].strftime("%d/%m/%Y - %H:%M")))
    print("Duração da corrida: {}".format(informacoes_corrida["tempo_total_corrida"]))
    print("Valor da corrida R$: {}".format(informacoes_corrida["valor_corrida"]))

def imprimir_extrato(informacoes_corrida):
    extrato_topo(informacoes_corrida)
    extrato_informacoes_corrida(informacoes_corrida)

if __name__ == "__main__":
    informacoes_corrida = {}
    informacoes_corrida["codigo_cliente"], informacoes_corrida["nome_cliente"] = cadastrar_Cliente()
    informacoes_corrida["dataHora_inicio_corrida"] = iniciar_corrida()
    informacoes_corrida["dataHora_fim_corrida"] = finalizar_corrida()
    informacoes_corrida["tempo_total_corrida"] = calcular_tempo_corrida(informacoes_corrida["dataHora_inicio_corrida"], informacoes_corrida["dataHora_fim_corrida"])
    informacoes_corrida["valor_corrida"] = calcular_valor_corrida(informacoes_corrida["tempo_total_corrida"])
    imprimir_extrato(informacoes_corrida)
