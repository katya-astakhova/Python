class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 200000, "bonus": 100000}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        income = self._income
        print(sum(income.values()))


c = Worker("Василий", "Иванов", "Менеджер")
b = Position("Василий", "Иванов", "Менеджер")
b.get_full_name()
b.get_total_income()
