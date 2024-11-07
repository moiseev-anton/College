class Point:
    def __init__(self, x: float, y: float):
        """Инициализация экзепляра точки"""
        self.x = x
        self.y = y

    def get_position(self):
        """Определяет положение точки на координатной плоскости"""
        if self.x > 0 and self.y > 0:
            return "I четверть"
        elif self.x < 0 and self.y > 0:
            return "II четверть"
        elif self.x < 0 and self.y < 0:
            return "III четверть"
        elif self.x > 0 and self.y < 0:
            return "IV четверть"
        elif self.x == 0 and self.y == 0:
            return "Точка в начале координат"
        elif self.x == 0:
            return "Точка на оси Y"
        elif self.y == 0:
            return "Точка на оси X"


if __name__ == "__main__":
    try:
        x = float(input("Введите координату x: "))
        y = float(input("Введите координату y: "))
        point = Point(x, y)
        position = point.get_position()
        print(position)
    except ValueError:
        print("Координата должна быть числом")

