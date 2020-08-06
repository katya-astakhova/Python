from itertools import count
from itertools import cycle


def func_count(n):
    for el in count(int(n[0])):
        if el > (int(n[1])):
            break
        else:
            print(el)


def func_cycle(nu):
    c = 0
    for i in cycle(nu[0]):
        if c > 5:
            break
        print(i)
        c += 1


num = input("Введите что-нибудь! ").split()
if num[0].isdigit():
    func_count(num)
else:
    func_cycle(num)
