class Stationery:
    def title(self):
        print("Рисунок")

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом")


class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером")


s = Stationery()
s.title()
s.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
