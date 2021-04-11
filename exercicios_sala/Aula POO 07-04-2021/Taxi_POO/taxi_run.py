from datetime import datetime, timedelta

class TaxiRun:
    def __init__(self, **kwargs):
        self._id = kwargs['id']
        self._datetime_start = None
        self._datetime_stop = None
        self._duration_in_minutes = None
        self._taxi_run_value = None
        self._address_start = kwargs['address_start']
        self._address_stop = kwargs['address_stop']
        self._latitude_start = kwargs['latitude_start']
        self._longitude_start = kwargs['longitude_start']
        self._latitude_stop = kwargs['latitude_stop']
        self._longitude_stop = kwargs['longitude_stop']
        self._route_lenght_in_meters = None
        self._client = kwargs['client']
        self._taxi_driver = kwargs['taxi_driver']
        self._taxi = kwargs['taxi']

    
    def iniciar_corrida(self):
        self._datetime_start = datetime.now()
    
    @property
    def datetime_start(self):
        return self._datetime_start
    
    def finalizar_corrida(self):
        # data_hora_termino = datetime.now()
        # somente para testar
        delta_tempo_mock = timedelta(hours=0, minutes=90, seconds=0)
        self._datetime_stop = datetime.now() + delta_tempo_mock
        self.calcular_duracao_corrida()
        self.calcular_valor_corrida()
    
    @property
    def datetime_stop(self):
        return self._datetime_stop
    
    def is_bandeira_01(self):
        if ((self._datetime_start.hour>22) and (self._datetime_start.hour<6)):
            return False
        else:
            return True
    
    def calcular_duracao_corrida(self):
        duracao_corrida = self._datetime_stop-self._datetime_start
        self._duration_in_minutes = int(duracao_corrida.seconds/60)
    
    @property
    def duration_in_minutes(self):
        return self._duration_in_minutes
    

    def calcular_valor_corrida(self):
        taxa_bandeira_2 = 1.2 
        valor_tarifa_inicio = 5.50
        valor_tarifa_minuto = 0.75
        if self.is_bandeira_01():
            self._taxi_run_value = (valor_tarifa_inicio + 
                (valor_tarifa_minuto * self._duration_in_minutes))
        else:
            self._taxi_run_value = (valor_tarifa_inicio + 
                (valor_tarifa_minuto * self._duration_in_minutes)) * taxa_bandeira_2
    
    @property
    def taxi_run_value(self):
        return self._taxi_run_value

    @property
    def client(self):
        return self._client
    
    @property
    def taxi_driver(self):
        return self._taxi_driver
    
    @property
    def taxi(self):
        return self._taxi
    
    # TODO: finalizar outros métodos