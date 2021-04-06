from datetime import datetime, timedelta

class corrida:
    def __init__(self partida, destino, tempo, datahoraini, datahorafim, distancia, bandeira, valor):
        self.partida = partida
        self.destino = destino
        self.tempo = tempo
        self.datahoraini = datahoraini
        self.datahorafim = datahorafim
        self.distancia = distancia
        self.bandeira = bandeira
        self.valor = valor

    def getTempo(self):
        return self.tempo

    def getDistancia(self):
        return self.distancia

    def getValor(self):
        return self.valor

    def getBandeira(self):
        return self.bandeira