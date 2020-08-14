class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polce = is_police


    def go(self):
        print("Car starts to move")

    def stop(self):
        print("Car stopped")

    def turn(self, direction):
        print(f'Car turns to {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print("Too FAST!")
        else:
            print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print("Too FAST!")
        else:
            print(self.speed)


class SportCar(Car):
    def cool(self):
        print("Cool car")


class PoliceCar(Car):
    def police(self):
        if self.is_polce is True:
            print("This is Police car!")
        else:
            print("This is NOT Police car LAIR!")


a = Car("70", "black", "Jeep", False)
a.show_speed()
a.turn("west")

b = TownCar("70", "black", "Jeep", False)
b.show_speed()

c = PoliceCar("70", "black", "Jeep", False)
c.police()
