class SimpleCalculator:
    @staticmethod
    def arithmetic(a: float, b: float, operation: str) -> float:
        """Выполняет арифметическую операцию над двумя числами"""
        if operation not in '+-*/':
            raise ValueError('Неизвестная операция')
        if operation == '/' and b == 0:
            raise ZeroDivisionError('Деление на ноль недопустимо')

        if operation == "+":
            return a + b
        if operation == "-":
            return a - b
        if operation == "*":
            return a * b
        if operation == "/":
            return a / b


if __name__ == '__main__':
    try:
        a = float(input("Введите первое число: "))
        operation = input("Введите операцию (+, -, *, /): ")
        b = float(input("Введите второе число: "))
        result = SimpleCalculator.arithmetic(a, b, operation)
        print(f"Результат операции {a} {operation} {b} = {result}")
    except Exception as e:
        print(e)


