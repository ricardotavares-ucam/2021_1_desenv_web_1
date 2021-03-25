from datetime import datetime, timedelta

# data_hora_inicio = datetime.now()
# print(data_hora_inicio)
# print(data_hora_inicio.strftime('%d/%m/%Y - %H:%M'))


data_hora_inicio = datetime.now()
delta_tempo_mock = timedelta(hours=0, minutes=90, seconds=0)
data_hora_termino = data_hora_inicio + delta_tempo_mock
duracao_corrida = data_hora_termino-data_hora_inicio
print(duracao_corrida)

duracao_corrida = int(duracao_corrida.seconds/60)
print(duracao_corrida)



# data_hora_inicio = datetime.now()
# delta_tempo_mock = timedelta(days = 1, hours=0, minutes=90, seconds=0)
# data_hora_termino = data_hora_inicio + delta_tempo_mock
# duracao_corrida = data_hora_termino-data_hora_inicio
# print(duracao_corrida)

# duracao_corrida = int(duracao_corrida.seconds/60)
# print(duracao_corrida)
