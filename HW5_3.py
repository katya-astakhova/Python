f = open('text_3.txt', 'r', encoding='utf-8')
s = 0.0
n = 0
for line in f:
    n += 1
    string = float(line.split()[1])
    if string < 20000:
        print(line.split()[0])
    s = (s + string)
print(f'{s/n:.2f}')
