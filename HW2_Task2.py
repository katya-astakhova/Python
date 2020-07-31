user_list = []
n = int(input("Введите количество элементов: "))

for i in range(0, n):
    el = input()
    user_list.append(el)
print(user_list)

for i in range(0, len(user_list)-1):
    if i%2 == 0:
        user_list[i], user_list[i+1] = user_list[i+1], user_list[i]

print(user_list)
