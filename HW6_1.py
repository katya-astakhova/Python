import time


class TrafficLight:
    color = "black"


    def running(self):
        print("red")
        time.sleep(7)
        print("yellow")
        time.sleep(2)
        print("green")
        time.sleep(7)


a = TrafficLight()
a.running()
