class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Чертят им или рисуют. Грифель по листку танцует.")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Пишем ей в тетрадку буквы по порядку.")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Я художник первоклассный, это всем ребятам ясно.")


st = Stationery("Канцелярские принадлежности")
st.draw()
pen = Pen("Карандаш")
pen.draw()
pencil = Pencil("Ручка")
pencil.draw()
handle = Handle("Маркер")
handle.draw()


