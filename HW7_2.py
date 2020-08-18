from abc import ABC, abstractmethod

class Cloth(ABC):
    @abstractmethod
    def faber(self):
        print("Понадобится ткани: ")

class Coat(Cloth):
    def __init__(self, size):
        self.size = size

    def faber(self):
        super().faber()
        print(f'{self.size/6.5 + 0.5:.1f}')

class Dress(Cloth):
    def __init__(self, height):
        self.height = height

    def faber(self):
        super().faber()
        print(2*self.height + 0.3)


a_1 = Coat(15)
a_1.faber()
a_2 = Dress(15)
a_2.faber()
