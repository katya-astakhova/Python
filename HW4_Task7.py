def fact(i):
    f = 1
    for j in range(1, i+1):
        f *= j
        yield f


n = int(input("Введите число "))
k = 1
for el in fact(n):
    print(f' {k}! = {el}')
    k += 1
