class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}+{self.b}j'

    def __add__(self, other):
        a_1 = self.a + other.a
        b_1 = self.b + other.b
        return Complex(a_1, b_1)

    def __mul__(self,other):
        a_2 = self.a * other.a - self.b * other.b
        b_2 = self.b * other.a + self.a * other.b
        return Complex(a_2, b_2)


c = Complex(1, 2)
d = Complex(1, 4)
print(c * d)
print(c + d)
