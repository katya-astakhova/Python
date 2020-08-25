class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def convert(cls, date):
        date = date.split('-')
        date = [int(item) for item in date]
        return cls(date)


    @staticmethod
    def valid(self):
        if (self.date[0] > 31) | (self.date[1] > 12) | (self.date[2] > 3000):
            return "Неверно"
        else:
            return self.date


inp = input("Введите дату в формате чч-мм-гггг ")
a = Date.convert(inp)
print(*a.valid(a))
