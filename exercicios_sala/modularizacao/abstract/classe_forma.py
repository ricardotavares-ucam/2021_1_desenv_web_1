# criar uma Base Class e forçar a implementação do método calc_area
# precisamos importar ABC (Abstract Base Class) e abstractmethod

from abc import ABC, abstractmethod


class Forma(ABC):
    def __init__(self):
        super().__init__()

    # indica que o método calc_area é um método abstrato,
    # e não existe nenhuma implementação nesse local.
    # Sendo que a implementação é obrigatória nas subclasses
    @abstractmethod
    def calc_area(self):
        pass
