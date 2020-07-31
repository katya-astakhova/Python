rate = [8, 7, 5, 5, 1]
value = int(input("Введите значение "))

for el in rate:
    if value > el:
        rate.insert(rate.index(el), value)
        print(rate)
        break
    elif value == el:
        rate.insert(rate.index(el)+1, value)
        print(rate)
        break
