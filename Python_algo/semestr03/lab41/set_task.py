# Класс для работы с множеством
class MySet:
    def __init__(self, elements=None):
        """Инициализация множества. Если не переданы элементы, создается пустое множество"""
        self.elements = set(elements) if elements else set()

    def contains(self, element) -> bool:
        """Проверка, содержит ли множество элемент"""
        return element in self.elements

    def union(self, other_set) -> 'MySet':
        """Объединение двух множеств"""
        return MySet(self.elements.union(other_set.elements))

    def intersection(self, other_set) -> 'MySet':
        """Пересечение двух множеств"""
        return MySet(self.elements.intersection(other_set.elements))

    def __str__(self):
        return f"{sorted(self.elements)}"


# Класс расписания, наследующийся от множества
class Schedule(MySet):
    def __init__(self):
        super().__init__()
        self.schedule = []  # Список для хранения расписания

    def add_course(self, day: str, number: int, course_name: str):
        """Добавление курса в расписание"""
        self.schedule.append({"day": day, "number": number, "course_name": course_name})

    def get_schedule(self) -> list:
        """Возвращает полное расписание на неделю"""
        return self.schedule

    def get_day_schedule(self, day: str) -> list:
        """Возвращает расписание на конкретный день"""
        return [course for course in self.schedule if course["day"] == day]

    def edit_course(self, day: str, number: int, new_course_name: str) -> bool:
        """
        Редактирование названия курса на конкретную пару в конкретный день.
        Возвращает True, если изменение произошло успешно, иначе False.
        """
        for course in self.schedule:
            if course["day"] == day and course["number"] == number:
                course["course_name"] = new_course_name
                return True
        return False

    def __str__(self) -> str:
        schedule_str = "Расписание:\n"
        for course in self.schedule:
            schedule_str += f"{course['day']} - Пара {course['number']}: {course['course_name']}\n"
        return schedule_str




if __name__ == "__main__":
    # Создаем расписание
    schedule = Schedule()

    # Добавляем пары
    schedule.add_course("Понедельник", 1, "Математика")
    schedule.add_course("Понедельник", 2, "Программирование")
    schedule.add_course("Вторник", 1, "Физика")
    schedule.add_course("Среда", 3, "Алгоритмы")

    # Просмотр всего расписания
    print(schedule)

    # Просмотр расписания на понедельник
    print("Расписание на понедельник:")
    for course in schedule.get_day_schedule("Понедельник"):
        print(f"Пара {course['number']}: {course['course_name']}")

    # Редактируем название курса
    schedule.edit_course("Понедельник", 1, "Высшая математика")
    print("\nПосле редактирования:")
    print(schedule)

