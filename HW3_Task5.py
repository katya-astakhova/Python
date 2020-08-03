def enter_func(ent):
    n = 0
    summa = 0
    a = ent.split()
    for i in a:
        if i.upper() == 'Q':
            n += 1
            break
        else:
            i = int(i)
            summa += i
    return summa, n


g = 0
s = 0
while True:
    if g == 1:
        break
    else:
        en = input("Вводите числа, для выхода нажать q ")
        pr, g = enter_func(en)
        s += pr
        if s > 0:
            print(s)
