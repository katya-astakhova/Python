lines = []
while True:
    _ = input('Вводите слова, для выхода из программы нажмите "Enter": ')
    if _ == '':
        break
    else:
        lines.append(_)

with open('textfile.txt', 'w', encoding='utf-8') as file:
    for line in lines:
       file.write(line + '\n')
