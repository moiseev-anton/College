class NumberDescriptor:
    "Дескриптор для натуральных числел"

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value <= 0 or not isinstance(value, int):
            raise ValueError(f"{self.name[1:]} должно быть натуральным числом.")
        setattr(instance, self.name, value)


class NumberPair:
    a = NumberDescriptor()
    b = NumberDescriptor()

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_gcd(self, a: int, b: int) -> int:
        """Вычисляет НОД"""
        while b != 0:
            a, b = b, a % b
        return a

    def get_lcm(self) -> int:
        """Вычисляет НОК"""
        return (self.a * self.b) // self.get_gcd(self.a, self.b)


if __name__ == "__main__":
    try:
        a = int(input("Введите первое натуральное число: "))
        b = int(input("Введите второе натуральное число: "))
        pair = NumberPair(a, b)

        print(f"НОК чисел {a} и {b} равно: {pair.get_lcm()}")

    except ValueError as e:
        print(e)
