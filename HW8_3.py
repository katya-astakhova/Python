class OnlyNumbers(Exception):
    def __init__(self, txt):
        self.txt = txt


n = 0
my_list = []
while True:
    if n == 1:
        break
    ent = input("Вводите числа, для выхода нажать q ")
    a = ent.split()
    for i in a:
        if i == 'stop':
            n += 1
            break
        try:
            if i.isdigit() == False:
                raise OnlyNumbers("Только числа!")
        except OnlyNumbers as err:
            print(err)
        else:
            my_list.append(i)
print(*my_list)
