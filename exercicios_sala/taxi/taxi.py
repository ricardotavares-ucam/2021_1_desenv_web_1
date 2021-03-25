#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

# Código para registrar corrida de taxi

def extrato_cabecalho(dados_corrida):
    print("=======================================================")
    print(" ***************** Extrato da Corrida ***************** ")
    print("=======================================================")
    print("Cód. cliente: {}".format(dados_corrida['codigo_cliente']))
    print("Nome cliente: {}".format(dados_corrida['nome_cliente']))
    print("=======================================================")

def extrato_rodape():
    print("=======================================================")
    print('Fatura emitida em: \t')
    print(datetime.now().strftime('%d/%m/%Y - %H:%M'))

def extrato_dados_corrida(dados_corrida):
    print('Início da corrida: {}'.format(dados_corrida['data_hora_inicio'].strftime('%d/%m/%Y - %H:%M')))
    print('Término da corrida: {}'.format(dados_corrida['data_hora_termino'].strftime('%d/%m/%Y - %H:%M')))
    print('Duração da corrida: {} minutos'.format(dados_corrida['duracao_corrida']))
    print('Valor da corrida: R$ {:.2f}'.format(dados_corrida['valor_corrida']))

def imprimir_extrato(dados_corrida):
    extrato_cabecalho(dados_corrida)
    extrato_dados_corrida(dados_corrida)
    extrato_rodape()

def iniciar_corrida():
    data_hora_inicio = datetime.now()
    return data_hora_inicio

def finalizar_corrida():
    # data_hora_termino = datetime.now()
    # somente para testar
    delta_tempo_mock = timedelta(hours=0, minutes=90, seconds=0)
    data_hora_termino = datetime.now() + delta_tempo_mock
    return data_hora_termino

def is_bandeira_01():
    if ((data_hora_inicio.hour>22) and (data_hora_inicio.hour<6)):
        return False
    else:
        return True

def calcular_duracao_corrida(data_hora_inicio, data_hora_termino):
    duracao_corrida = data_hora_termino-data_hora_inicio
    duracao_corrida = int(duracao_corrida.seconds/60)
    return duracao_corrida

def calcular_valor_corrida(duracao_corrida):
    taxa_bandeira_2 = 1.2 
    valor_tarifa_inicio = 5.50
    valor_tarifa_minuto = 0.75
    if is_bandeira_01:
        valor_corrida = valor_tarifa_inicio + (valor_tarifa_minuto * duracao_corrida)
    else:
        valor_corrida = (valor_tarifa_inicio + (valor_tarifa_minuto * duracao_corrida)) * taxa_bandeira_2
    return valor_corrida

def cadastrar_cliente():
    codigo_cliente = int(input('Favor digite o código do cliente: '))
    nome_cliente = input('Favor digite o nome do cliente: ')
    return codigo_cliente, nome_cliente


if __name__ == '__main__':
    dados_corrida = {}
    dados_corrida['codigo_cliente'], dados_corrida['nome_cliente'] = cadastrar_cliente()
    dados_corrida['data_hora_inicio'] = iniciar_corrida()
    dados_corrida['data_hora_termino'] = finalizar_corrida()
    dados_corrida['duracao_corrida'] = calcular_duracao_corrida(dados_corrida['data_hora_inicio'], 
        dados_corrida['data_hora_termino'])
    dados_corrida['valor_corrida'] = calcular_valor_corrida(dados_corrida['duracao_corrida'])
    imprimir_extrato(dados_corrida)

