a = int(input("Введите число"))
a = a//10
ost = a%10
while a>0:
    if a%10 > ost:
       ost = a%10
    a = a//10
print(ost)
