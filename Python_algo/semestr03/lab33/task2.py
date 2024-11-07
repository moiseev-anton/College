class Person:
    # Атрибуты класса (распространяются на все экземпляры)
    AVERAGE_INCOME = 0
    AVERAGE_EXPENSE = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_income(self):
        print(f"Получен доход: {self.AVERAGE_INCOME} денежных единиц.")

    def print_expense(self):
        print(f"Потрачено: {self.AVERAGE_EXPENSE} денежных единиц.")

    def __str__(self):
        return f"{self.name}, {self.age} лет, {self.gender}"


# Мы можем использовать методы базового класса в качетсве интерфейса
# и просто перегрузить атрибуты(дохода и расхода) класса для дочерних классов
class Preschooler(Person):
    AVERAGE_INCOME = 0
    AVERAGE_EXPENSE = 2000


class Pupil(Person):
    AVERAGE_INCOME = 500
    AVERAGE_EXPENSE = 3000


class Student(Person):
    AVERAGE_INCOME = 8000
    AVERAGE_EXPENSE = 15000


class Worker(Person):
    AVERAGE_INCOME = 50000
    AVERAGE_EXPENSE = 40000


if __name__ == "__main__":
    while True:
        while True:
            try:
                full_name = input("Введите полное имя (или 'выход' для завершения): ")
                if full_name.lower() == 'выход':
                    break
                age = int(input("Введите возраст: "))
                gender = input("Введите пол: ")

                print("\nВыберите категорию:")
                print("1. Дошкольник")
                print("2. Школьник")
                print("3. Студент")
                print("4. Работающий человек")
                print("5. Выход")
                choice = int(input("Ваш выбор (1-5): "))

                # Создаем экземпляр в соответсвии с выбором
                if choice == 1:
                    person = Preschooler(full_name, age, gender)
                elif choice == 2:
                    person = Pupil(full_name, age, gender)
                elif choice == 3:
                    person = Student(full_name, age, gender)
                elif choice == 4:
                    person = Worker(full_name, age, gender)
                elif choice == 5:
                    print("Выход из программы.")
                    break
                else:
                    print("Неправильный выбор.")
                    continue

                print(f"\nИнформация о человеке: {person}")
                # Вызываем методы для созданного экземпляра
                person.print_income()
                person.print_expense()

            except ValueError:
                print("Ошибка ввода данных. Пожалуйста, введите корректные значения.")

