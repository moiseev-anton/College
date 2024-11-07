class Transport:
    """Родительский класс транспорта"""
    pass


class LandTransport(Transport):
    """Класс наземного транспорта"""
    pass


class AirTransport(Transport):
    """Класс авиатранспорта"""
    pass


class Airplane(AirTransport):
    """Класс самолетов. Дочерний класс авиатранспорта"""
    pass


class Helicopter(AirTransport):
    """Класс вертолетов. Дочерний класс авиатранспорта"""
    pass


class WaterTransport(Transport):
    """Класс водного транспорта"""
    pass


class Ship(WaterTransport):
    """Класс кораблей. Дочерний класс водного транспорта"""
    pass


class Boat(WaterTransport):
    """Класс лодок. Дочерний класс водного транспорта"""
    pass


class RailTransport(LandTransport):
    """Класс рельсового транспорта. Дочерний класс наземного транспорта"""
    pass


class CycleTransport(LandTransport):
    """Класс двухколесного транспорта. Дочерний класс наземного транспорта"""


class Bicycle(CycleTransport):
    """Класс велосипедов. Дочерний класс двухколесного транспорта"""
    pass


class Motorcycle(CycleTransport):
    """Класс мотоциклов. Дочерний класс двухколесного транспорта"""
    pass


class Car(LandTransport):
    """Класс автомобилей. Дочерний класс наземного транспорта"""
    pass


class PassengerCar(Car):
    """Класс легковых автомобилей. Дочерний класс автомобилей"""
    pass


class Truck(Car):
    """Класс грузовых автомобилей. Дочерний класс автомобилей"""
    pass

