def s_max(a, b, c):
    if a > b:
        if c > b:
            my_sum = a + c
        else:
            my_sum = a + b
    elif (a < b) & (c < b):
        my_sum = b + a
    else:
        my_sum = b + c
    return my_sum


print(s_max(int(input("Введите первое число ")), int(input("Введите второе число ")),
            int(input("Введите третье число "))))
