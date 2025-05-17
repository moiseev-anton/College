class LibraryItem:
    """Базовый класс для единиц хранения в библиотеке."""
    _inventory_counter = 1  # Автоинкремент инвентарного номера

    def __init__(self, title: str, in_stock: int, reading_room: bool):
        super().__init__()
        self.title = title
        self.inventory_number = LibraryItem._inventory_counter
        LibraryItem._inventory_counter += 1
        self.in_stock = in_stock  # Количество экземпляров в фонде
        self.reading_room = reading_room  # Признак, что объект доступен только в читальном зале
        self.borrowed_by = {}  # Словарь: {пользователь: количество}

    def take(self, user: str, quantity: int = 1):
        """Выдача единицы хранения пользователю."""
        if self.reading_room:
            print(f"{self.title} доступен только в читальном зале.")
            return
        if self.in_stock >= quantity:
            self.in_stock -= quantity
            self.borrowed_by[user] = self.borrowed_by.get(user, 0) + quantity
            print(f"{quantity} экземпляр(ов) {self.title} выдано {user}.")
        else:
            print(f"Недостаточно экземпляров {self.title} в наличии.")

    def return_item(self, user: str, quantity: int = 1):
        """Возврат единицы хранения пользователем."""
        if user in self.borrowed_by and self.borrowed_by[user] >= quantity:
            self.borrowed_by[user] -= quantity
            if self.borrowed_by[user] == 0:
                del self.borrowed_by[user]
            self.in_stock += quantity
            print(f"{quantity} экземпляр(ов) {self.title} возвращено {user}.")
        else:
            print(f"{user} не имеет {quantity} экземпляра(ов) {self.title} на руках.")

    def display_info(self):
        """Вывод информации об объекте."""
        print(f"Название: {self.title}")
        print(f"Инвентарный номер: {self.inventory_number}")
        print(f"В наличии: {self.in_stock}")
        print(f"Читальный зал: {'Да' if self.reading_room else 'Нет'}")
        print("Выдано:")
        for user, count in self.borrowed_by.items():
            print(f"  {user}: {count} экземпляр(ов)")


class Book(LibraryItem):
    """Класс для книги"""
    def __init__(self, title: str, author: str, year: int, in_stock: int, reading_room: bool, rental_price: float):
        super().__init__(title, in_stock, reading_room)
        self.author = author
        self.year = year
        self.rental_price = rental_price

    def display_info(self):
        """Вывод информации о книге."""
        super().display_info()
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")
        print(f"Цена аренды: {self.rental_price:.2f} руб.")


class SubscribableMixin:
    """Миксин для добавления функциональности подписки"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subscribers = set()

    def subscribe(self, user: str):
        """Добавление пользователя в список подписчиков."""
        self.subscribers.add(user)
        print(f"{user} подписан на {self.title}.")

    def display_info(self):
        """Вывод информации об объекте с подписчиками."""
        super().display_info()
        print("Подписчики:")
        for subscriber in self.subscribers:
            print(f"  - {subscriber}")


class Magazine(SubscribableMixin, LibraryItem):
    """Класс для журнала, поддерживающий подписку"""
    def __init__(self, title: str, issue_number: int, articles: list, in_stock: int, reading_room: bool):
        # Вызываем `super()` для всех базовых классов
        super().__init__(title=title, in_stock=in_stock, reading_room=reading_room)
        self.issue_number = issue_number
        self.articles = articles

    def display_info(self):
        """Вывод информации о журнале."""
        super().display_info()
        print(f"Номер выпуска: {self.issue_number}")
        print("Статьи:")
        for article in self.articles:
            print(f"  - {article}")


if __name__ == "__main__":
    # Создаем книгу
    book = Book(title="1984", author="Джордж Оруэлл", year=1949, in_stock=5, reading_room=False, rental_price=10.0)
    book.display_info()
    print()
    # Получение и возврат
    book.take('Алина', 2)
    book.return_item('Алина', 1)
    print()
    book.display_info()
    print()

    # Создаем журнал
    magazine = Magazine(title="National Geographic", issue_number=12, articles=["Наука", "Природа"],
                                    in_stock=3, reading_room=True)
    magazine.display_info()
    print()
    # Подписка на журнал
    magazine.subscribe('Иван')
    magazine.subscribe('Алина')
    print()

    magazine.display_info()

