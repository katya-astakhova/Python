def int_func(word):
    f_let = word[0]
    f_let_cap = chr(ord(f_let) - ord('a') + ord('A'))
    return f_let_cap + word[1:]



s = input("Введите несколько слов латинскими буквами ").split(' ')
for el in s:
    print(f"{int_func(el)} ", end='')
