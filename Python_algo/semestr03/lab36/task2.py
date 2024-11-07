class Employee:
    # Атрибуты класса используем как константы
    MINIMUM_WAGE = 16000  # МРОТ (примерно).
    TAX_COEF = 0.13  # налог

    def __init__(self, full_name, age, salary):
        self.full_name = full_name
        self.age = age
        self.salary = salary

    # Реализуем свойство property для ЗП.
    # Это позволит сделать сеттер для корректного изменения атрибута
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < self.MINIMUM_WAGE:
            raise ValueError(f"ЗП не может быть меньше МРОТ: {Employee.MINIMUM_WAGE} руб")
        self._salary = value

    @property
    def tax(self):
        """Рассчитывает подоходный налог 13%"""
        return self.salary * Employee.TAX_COEF

    # Перегружаем дандер методы для сравнения экземпляров
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.salary == other.salary
        return False

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.salary < other.salary
        return False

    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.salary > other.salary
        return False

    # перегружаем дандер метод для отображения информации о экземпляре
    def __str__(self):
        return f"Сотрудник: {worker1.full_name}, Возраст: {worker1.age}, ЗП: {worker1.salary:.2f} руб."


if __name__ == '__main__':
    # Создание объектов работников
    worker1 = Employee("Иванов Иван Иванович", 30, 50000)
    worker2 = Employee("Петров Петр Петрович", 28, 60000)

    # Вывод информации о работниках
    print(worker1)
    print(worker2)

    # Сравниваем экземпляры работников (по зарплате)
    if worker1 == worker2:
        print('Заработная плата работников одинакова')
    elif worker1 > worker2:
        print('Заработная плата первого работника больше')
    else:
        print('Заработная второго работника больше')

    # Расчет подоходного налога
    print(f"Налог для работника 1: {worker1.tax:.2f} руб.")
    print(f"Налог для работника 2: {worker2.tax:.2f} руб.")

    # Изменение заработной платы
    try:
        worker1.salary = 15000  # Это ниже МРОТ, вызовет ошибку
    except ValueError as e:
        print(e)

