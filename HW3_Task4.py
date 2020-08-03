def pow_func(x, y):
    res = 0
    if (x > 0) & (y < 0) & (y % 2 == 0):
        for i in range(abs(y)):
            res = x * x
        return 1/res
    else:
        return "Соблюдайте условия!"


print(pow_func(float(input("Введите положительное число ")), int(input("Введите целое отрицательное число "))))
