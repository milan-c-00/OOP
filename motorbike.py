class Motorbike:
    def __init__(self, speed):
        print("Motorbike instance created!")
        self.speed = speed

    def increase_speed(self, how_much):
        self.speed += how_much

    def decrease_speed(self, how_much):
        self.speed -= how_much


honda = Motorbike(50)
ducati = Motorbike(250)

print(honda.speed)
print(ducati.speed)

honda.increase_speed(150)
ducati.increase_speed(25)

print(honda.speed)
print(ducati.speed)

honda.decrease_speed(50)
ducati.decrease_speed(35)

print(honda.speed)
print(ducati.speed)

