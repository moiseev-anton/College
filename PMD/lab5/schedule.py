from typing import Any

from my_set import MyHashSet


class ScheduleSet(MyHashSet):
    """
    Класс расписания уроков.
    Дочерний для MyHashSet
    """

    WEEK_DAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']

    def display_week(self) -> None:
        """Выводит расписание на всю неделю"""
        for day in self.WEEK_DAYS:
            self.display_day(day)

    def display_day(self, day: str) -> None:
        """Выводит расписание уроков на конкретный день недели"""
        lessons = sorted([l for l in self if l.day == day], key=lambda x: x.class_number)
        if lessons:
            print(f"\n{day}:")
            for lesson in lessons:
                print(lesson.display())

    def edit_course_name(self, day: str, class_number: int, new_name: str) -> bool:
        """Изменяет название урока в расписании"""
        lesson = Lesson(day, class_number, new_name)  # Временный объект для поиска
        if lesson in self:
            self.remove(lesson)  # Удаляем старый урок
            self.add(lesson)  # Добавляем новый урок с измененным именем
            return True
        return False


class Lesson:
    """Класс урока"""

    def __init__(self, day: str, class_number: int, course_name: str) -> None:
        self.day = day
        self.class_number = class_number
        self.course_name = course_name

    def __eq__(self, other: Any) -> bool:
        """
        Определяет, является ли другой объект эквивалентным текущему уроку.
        Эквивалентность основана на дне недели и номере урока
        """
        if isinstance(other, Lesson):
            return (self.day, self.class_number) == (other.day, other.class_number)
        return False

    def __hash__(self) -> int:
        """Возвращает хеш урока, основанный на дне недели и номере урока"""
        return hash((self.day, self.class_number))

    def __str__(self) -> str:
        """Строковое представление урока полностью"""
        return f'{self.day} {self.class_number} урок: {self.course_name}'

    def display(self):
        """Представление урока (№ урока, Название)"""
        return f'{self.class_number}: {self.course_name}'


if __name__ == '__main__':
    schedule = ScheduleSet()
    schedule.add(Lesson("Понедельник", 1, "Математика"))
    schedule.add(Lesson("Понедельник", 2, "Физика"))
    schedule.add(Lesson("Среда", 1, "Математика"))
    schedule.add(Lesson("Пятница", 2, "Физика"))
    schedule.add(Lesson("Четверг", 1, "Химия"))
    schedule.add(Lesson("Вторник", 1, "Биология"))

    print("На неделю:")
    schedule.display_week()
    print('===================')

    print("На день:")
    schedule.display_day('Понедельник')

    schedule.edit_course_name("Понедельник", 1, "Алгебра")

    print('===================')
    print("После изменений:")
    schedule.display_day('Понедельник')
