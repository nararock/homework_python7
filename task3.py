class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


p1 = Position("Hector", "Kappaldi", "manager", 21500, 1200)
print(f"fullname: {p1.get_full_name()}")
print(f"income: {p1.get_total_income()}")
print(f"position: {p1.position}")
p2 = Position("Funny", "Kaplan", "seller", 12500, 550)
print(f"fullname: {p2.get_full_name()}")
print(f"income: {p2.get_total_income()}")
print(f"position: {p2.position}")
