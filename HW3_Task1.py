def div(a, b):
    if b != 0:
        return f"{a / b:.2f}"
    else:
        return "На ноль не делим!"


print(div(float(input("Введите первое число ")), float(input("Введите второе число "))))
