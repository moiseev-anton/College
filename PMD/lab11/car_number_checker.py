import re


class CarNumberChecker:
    """Класс для проверки регистрационных номеров"""

    PATTERNS = {
        'Privat': r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$',
        'Taxi': r'^[АВЕКМНОРСТУХ]{2}\d{5,6}$',
    }

    def check(self, plate):
        for key, pattern in self.PATTERNS.items():
            if re.match(pattern, plate):
                return key
        return "Fail"


if __name__ == "__main__":
    checker = CarNumberChecker()

    plates = [
        "А123ВС77",  # Privat
        "Х567УХ99",  # Privat
        "ТС23477",  # Taxi
        "МН123456",  # Taxi
        "AB123CD99",  # Fail
    ]

    for plate in plates:
        print(f"{plate}: {checker.check(plate)}")


