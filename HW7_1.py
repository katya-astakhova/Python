class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])


    def __add__(self, other):
        return list(map(lambda x, y: list(map(lambda z, w: z + w, x, y)), self.matrix, other.matrix))




a_1 = Matrix([[1, 2, 3],[4, 5, 6], [1, 1, 1]])
a_2 = Matrix([[9, 8, 7],[6, 5, 4], [3, 2, 1]])
print(a_1.__str__())
print("")
print(Matrix(a_1 + a_2))
