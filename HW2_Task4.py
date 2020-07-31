strip = input("Введите строку ")
word = strip.split(' ')

for ind, el in enumerate(word):
    if len(el) < 10:
        print(f"{ind+1}: {el}")
    elif len(el) >= 10:
        print(f"{ind+1}: {el [0:10]}")
