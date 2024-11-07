
# Для этой задачи мы можем расширить тип float новым методом в дочернем классе
class MyFloat(float):

    def get_rounded(self) -> int:
        """Округляет число"""
        if self < 0:
            raise ValueError("Округляются только неотрицательные числа")

        integer = int(self)
        fract = self - integer
        return integer if fract < 0.5 else integer + 1


if __name__ == "__main__":
    try:
        x = MyFloat(input("Введите число: "))
        result = x.get_rounded()
        print(result)
    except ValueError as e:
        print(e)

