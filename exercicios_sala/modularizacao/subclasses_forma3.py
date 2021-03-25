from abstract import classe_forma as cls_forma


class Circulo(cls_forma.Forma):
    def __init__(self, raio):
        self._raio = raio

    def calc_area(self):
        PI = 3.14
        return PI * (self._raio ** 2)


class Quadrado(cls_forma.Forma):
    def __init__(self, aresta):
        self._aresta = aresta

    def calc_area(self):
        return (self._aresta * self._aresta)


# forma = cls_forma.Forma()
circulo = Circulo(10)
print(circulo.calc_area())
quadrado = Quadrado(10)
print(quadrado.calc_area())
