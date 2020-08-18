class Cell:
    def __init__(self, unit):
        self.unit = unit

    def __add__(self, other):
        l = self.unit + other.unit
        return(l)

    def __sub__(self, other):
        st = ""
        if len(self.unit) > len(other.unit):
            for i in range(len(self.unit) - len(other.unit)):
                st = st + "*"
            return(st)
        else:
            return "Получается отрицательное число!"

    def __mul__(self, other):
        st = ""
        for i in range(len(self.unit) * len(other.unit)):
            st = st + "*"
        return(st)

    def __floordiv__(self, other):
        st = ""
        if len(self.unit) % len(other.unit) == 0:
            for i in range(len(self.unit) // len(other.unit)):
                st = st + "*"
            return(st)
        else:
            return "Не делится целочисленно"

    def make_order(self, a):
        st = ""
        l = len(self.unit)
        my_list = ""
        for i in range(l):
            st = st + "*"
            if (len(st) == int(a)) & (i < (((len(self.unit))//int(a))*int(a))):
                print(st)
                st = ""
            elif i == (l-1):
                print(st)



a_1 = Cell("**********")
a_2 = Cell("***")
a_1.make_order(7)
#print(a_1 - a_2)
