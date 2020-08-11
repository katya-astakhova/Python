f = open('textfile_2.txt', 'w', encoding='utf-8')
f.writelines(['20 ', '2 ', '6 '])
f = open('textfile_2.txt', 'r', encoding='utf-8')
st = f.readline().split()
s = 0
for el in st:
    s = s + int(el)
print(s)
