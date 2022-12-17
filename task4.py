class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direc):
        print(f"{self.name} повернула {direc}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Вы превышаете скорость!")
            return self.speed
        else:
            return self.speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Вы превышаете скорость!")
            return self.speed
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


tc = TownCar(45, "yellow", "BMW", False)
sc = SportCar(100, "silver", "Porsche", False)
wc = WorkCar(55, "black", "LADA", False)
pc = PoliceCar(0, "blue", "UAZ", True)
direction = "направо"

print(f"марка: {tc.name}, цвет: {tc.color}")
print("не является полицейской машиной") if not tc.is_police \
    else print("является полицейской машиной")
tc.go()
print(f"скорость: {tc.show_speed()} км/ч")


print(f"марка: {sc.name}, цвет: {sc.color}")
print("не является полицейской машиной") if not sc.is_police \
    else print("является полицейской машиной")
sc.turn(direction)
print(f"скорость: {sc.show_speed()} км/ч")


print(f"марка: {wc.name}, цвет: {wc.color}")
print("не является полицейской машиной") if not wc.is_police \
    else print("является полицейской машиной")
wc.go()
print(f"скорость: {wc.show_speed()} км/ч")


print(f"марка: {pc.name}, цвет: {pc.color}")
print("не является полицейской машиной") if not pc.is_police \
    else print("является полицейской машиной")
pc.stop()
print(f"скорость: {pc.show_speed()} км/ч")
