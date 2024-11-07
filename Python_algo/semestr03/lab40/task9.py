from abc import ABC, abstractmethod


class Animal(ABC):
    """Абстрактный класс животных"""

    def __init__(self, name: str, predator: bool):
        self.name = name
        self.predator = predator

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def predator(self) -> bool:
        return self._predator

    @name.setter
    def predator(self, predator: bool):
        self._predator = predator

    @abstractmethod
    def get_description(self):
        """Абстрактный метод для формирования описания животного"""
        pass


class Fish(Animal):
    """Класс рыб, наследуется от Animal"""

    def __init__(self, name: str, predator: bool, deep_water: bool):
        super().__init__(name, predator)
        self.deep_water = deep_water

    # добавляем свойсвтво Глубоководность
    @property
    def deep_water(self) -> bool:
        return self._deep_water

    @deep_water.setter
    def deep_water(self, value: bool):
        self._deep_water = value

    # перегружаем метод формирования описания
    def get_description(self) -> str:
        deep_water_status = 'глубоководная' if self.deep_water else 'не глубоководная'
        predator_status = 'да' if self.predator else 'нет'
        return f'Класс: {deep_water_status} рыба\nНазвание: {self.name}\nХищник: {predator_status}'


class Bird(Animal):
    """ Класс для птиц, наследуется от Animal """

    def __init__(self, name, flight_speed):
        super().__init__(name, False)
        self.flight_speed = flight_speed

    # добавляем свойсвтво Скорость полета
    @property
    def flight_speed(self) -> int:
        return self._flight_speed

    @flight_speed.setter
    def flight_speed(self, value: int):
        self._flight_speed = value

    # перегружаем метод формирования описания
    def get_description(self) -> str:
        return f'Класс: птица\nНазвание: {self.name}\nСкорость полета: {self.flight_speed} км/ч'


class Beast(Animal):
    """ Класс зверей, наследуется от Animal"""

    def __init__(self, name: str, predator: bool, habitat: str):
        super().__init__(name, predator)
        self.habitat = habitat

    @property
    def habitat(self) -> str:
        return self._habitat

    @habitat.setter
    def habitat(self, value: str):
        self._habitat = value

    # перегружаем метод формирования описания
    def get_description(self) -> str:
        predator_status = "да" if self.predator else "нет"
        return f'Класс: зверь\nНазвание: {self.name}\nСреда обитания: {self.habitat}\nХищник: {predator_status}'


class Cage:
    """ Класс вольера """

    def __init__(self, number: int, size: float, max_animals: int):
        self.number = number
        self.size = size
        self.max_animals = max_animals
        self.animals: list[Animal] = []  # наглядное следование LSP (принципу подстановки Барабары Лисков), полиморфизму

    def add_animal(self, animal: Animal) -> bool:
        """ Добавляет животное в вольер, если не превышен лимит и вольер не содержит животных другого типа """
        if len(self.animals) >= self.max_animals:
            print(f'Вольер {self.number} полон, животное не может быть добавлено')
            return False

            # Проверка на то, чтобы все животные в вольере были одного типа
        if self.animals and type(animal) != type(self.animals[0]):
            print(f'Вольер {self.number} не может содержать разные типы животных')
            return False

        self.animals.append(animal)
        return True

    def show_animals(self):
        """ Выводит информацию о всех животных в вольере """
        print(f'Вольер №{self.number}, размер: {self.size} кв.м, животных: {len(self.animals)} / {self.max_animals}')
        for animal in self.animals:
            print(animal.get_description())
            print("-" * 40)


class Zoo:
    """ Класс зоопарка """

    def __init__(self, name: str) -> None:
        self.name = name
        self.cages: list[Cage] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def add_cage(self, cage: Cage):
        self.cages.append(cage)

    def show_zoo(self):
        print(f"Зоопарк: {self.name}")
        for cage in self.cages:
            cage.show_animals()



if __name__ == "__main__":
    # Создаем зоопарк
    zoo = Zoo('Центральный')

    # Создаем вольеры
    cage1 = Cage(1, 100.0, 2)
    cage2 = Cage(2, 50.0, 1)
    cage3 = Cage(3, 75, 3)

    # Создаем животных
    beast = Beast('Волк', True, 'лес')  # Хищник с заданным ареалом обитания
    bird = Bird('Орел', 90)  # Птица с заданой скоростью полета
    fish = Fish('Удильщик', True, True)  # Хищная глубоководная рыба

    # Добавляем животных в вольеры
    cage1.add_animal(beast)
    cage2.add_animal(bird)
    cage3.add_animal(fish)

    # Добавляем вольеры в зоопарк
    zoo.add_cage(cage1)
    zoo.add_cage(cage2)
    zoo.add_cage(cage3)

    # Показываем информацию о всех животных в зоопарке
    zoo.show_zoo()

