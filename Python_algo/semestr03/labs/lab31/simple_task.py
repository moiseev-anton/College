class Cube:
    def __init__(self, side_length: float):
        """Инициализация экземпляра куба"""
        if side_length < 0:
            raise ValueError('Сторона не может быть отрицательной')
        self.side_length = side_length

    def get_face_area(self):
        """Вычисление площади грани"""
        return self.side_length ** 2

    def get_surfase_area(self):
        """Вычисление площади поверхности"""
        return self.get_face_area() * 6

    def get_volume(self):
        """Вычисление объема"""
        return self.side_length ** 3


if __name__ == '__main__':
    try:
        side_length = float(input("Введите длину стороны куба: "))
        cube = Cube(side_length)
        print(f"Площадь грани: {cube.get_face_area()}")
        print(f"Площадь поверхности: {cube.get_surfase_area()}")
        print(f"Объем: {cube.get_volume()}")
    except Exception as e:
        print(e)
