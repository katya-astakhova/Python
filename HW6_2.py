class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def needed(self):
        print(f'{self._length}м*{self._width}м*25кг*15см={(int(self._length)*int(self._width)*25*0.15)/1000} кг')


a = Road("1000", "55")
a.needed()
