class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __del__(self):
        """Деструктор, вызывается при удалении объекта"""
        print(f"Объект с временем {self} уничтожен")

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, value):
        if value < 0:
            raise ValueError('Секунды не могут быть отрицательными')
        self._seconds = value % 60
        minutes = value // 60
        if minutes:
            self.minutes += minutes

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        if value < 0:
            raise ValueError("Минуты не могут быть отрицательными!")
        self._minutes = value % 60
        hours = value // 60
        if hours:
            self.hours += hours

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        if value < 0:
            raise ValueError("Часы не могут быть отрицательными!")
        self._hours = value

    def total_seconds(self):
        """Вычисляет количество секунд"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def add_five_seconds(self):
        """Увеличивает время на 5 секунд"""
        self.seconds += 5

    def __str__(self):
        return f"⏱ {self.hours:02}:{self.minutes:02}:{self.seconds:02}"


if __name__ == '__main__':
    # создадим объекты
    t1 = Time(1, 30, 15)
    t2 = Time(12, 59, 58)
    h = int(input("Введите часы: "))
    m = int(input("Введите минуты: "))
    s = int(input("Введите секунды: "))
    t3 = Time(h, m, s)

    # выведем время объектов и количество секунд
    print(f"Объект t1: {t1}")
    print(f"Количество секунд в t1: {t1.total_seconds()}")

    print(f"Объект t2: {t2}")
    print(f"Количество секунд в t2: {t2.total_seconds()}")

    print(f"Объект t3: {t3}")
    print(f"Количество секунд в t3: {t3.total_seconds()}")

    # увеличиваем время t3 на 5 секунд
    t3.add_five_seconds()
    print(f"t3 после увеличения на 5 секунд: {t3}")

