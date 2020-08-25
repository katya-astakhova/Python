class DividedZero(Exception):
    def __init__(self, txt):
        self.txt = txt


i = input("")
b = i.split('/')

try:

    if int(b[1]) == 0:
        raise DividedZero("На 0 делить нельзя!")
except DividedZero as err:
    print(err)
else: print(f'{int(b[0])//int(b[1])}')
