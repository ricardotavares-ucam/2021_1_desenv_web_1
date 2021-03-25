from abstract import classe_forma as cls_forma


class Circulo(cls_forma.Forma):
    def __init__(self, raio):
        self._raio = raio


class Quadrado(cls_forma.Forma):
    def __init__(self, aresta):
        self._aresta = aresta


# forma = cls_forma.Forma()
circulo = Circulo(10)
print(circulo.calc_area())
quadrado = Quadrado(10)
print(quadrado.calc_area())
