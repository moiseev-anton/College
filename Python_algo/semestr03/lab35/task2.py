class CitiesGame:
    def __init__(self):
        self.words_set = set()  # Множество для хранения уникальных слов
        self.target_letter = ''  # Атрибут хранящий текущую буквы

    def add_word(self, word: str) -> bool:
        """Добавляет слово в множество, если оно корректно"""
        if self.words_set and word[0] != self.target_letter:
            raise ValueError('Неправильно')

        if word in self.words_set:
            raise ValueError("Cлово уже использовалось")

        self.words_set.add(word)
        self.set_target_letter(word)
        return True

    def set_target_letter(self, word: str) -> str:
        """Обновляет текущую букву"""
        valid_letter = word.rstrip(' ьъы')[-1]
        if valid_letter:
            setattr(self, 'target_letter', valid_letter)
        return valid_letter


if __name__ == "__main__":
    game = CitiesGame()

    word = input("Введите слово ('Стоп' для завершения): ").lower().strip()
    while True:
        if word == "стоп":
            break  # Завершаем игру при вводе "Стоп"

        try:
            if game.add_word(word):
                print("Правильно")
        except ValueError as e:
            print(e)

        print(f'\nВам на {game.target_letter.upper()}')
        word = input("Введите слово: ").lower().strip()

    print("Игра завершена")

