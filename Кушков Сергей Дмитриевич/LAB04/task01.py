#/usr/bin/env python3

MAX_VALID_SPEED = 90
MAX_CAPACITY = 4
MANDATORY_TIPS = 2500
PATH_ARROW = "->"
STOP_STATIONS: tuple =(
    "Ж/д станция Новый Петергоф",
    "Сашинская дорога",
    "Сашинская улица",
    "Гаражи",
    "Мельничная улица",
    "Родниковый переулок",
    "Улица Штакеншнейдера (д. Санино)",
    "Жилгородок",
    "Низино",
    "Подгорная улица",
    "Центральная улица",
    "Церковь",
    "Дорога на Бельведер",
    "Сашино",
    "Городское кладбище",
    "Улица Шахматова",
    "Универсам",
    "Университетский проспект",
    "Чебышёвская улица"
)
BASE_TARIFF_PER_VALUE = 200

BASE_DICT: dict[str, int] = {"speed": 100, "capacity":0}

class Transport:
    """Базовый класс транспортного средства со скоростью и вместимостью."""


    def __init__(self, speed, capacity):
        """
        Инициализирует экземпляр транспортного средства.

        :param speed: Скорость транспорта.
        :param capacity: Вместимость транспорта.
        """
        self._speed = 0
        self._capacity = 0
        self.speed: int = speed
        self.capacity: int = capacity


    @property
    def speed(self):
        """Возвращает текущую скорость транспорта."""
        return self._speed

    @speed.setter
    def speed(self, speed):
        """
        Устанавливает новое значение скорости (не может быть отрицательным).

        :param speed: Новая скорость транспорта.
        """
        if speed >= 0:
            self._speed = speed
        else:
            print(f"\n{self.__class__.__name__}: Speed value must be positive")

    @property
    def capacity(self):
        """Возвращает текущую вместимость транспорта."""
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Устанавливает новое значение вместимости (не может быть отрицательным).

        :param capacity: Новая вместимость транспорта.
        """
        if capacity >= 0:
            self._capacity = capacity
        else:
            print(f"\n{self.__class__.__name__}: Capacity value must be positive")

    def __str__(self):
        """Выводит в консоль информацию о типе транспорта, его скорости и вместимости."""
        return f"\n{self.__class__.__name__}: Скорость {self._speed} и вместимость {self._capacity}"

    def speed_check(self):
        """
        Проверяет, не превышает ли скорость допустимый порог в 90 км/ч.

        :return: True, если скорость превышена, иначе False.
        """
        speed_too_high_warning: bool = False
        if self._speed > MAX_VALID_SPEED:
            print(f"\n{self.__class__.__name__}: Вы превысили допустимую скорость")
            speed_too_high_warning = True

        return speed_too_high_warning

    @classmethod
    def from_dict(cls, usr_dict):
        """
        Создаёт объект транспорта из словаря с параметрами.

        :param usr_dict: Словарь с ключами 'speed' и 'capacity'.
        :return: Новый экземпляр класса Transport.
        """
        speed = usr_dict.get("speed", 0)
        capacity = usr_dict.get("capacity", 0)
        return cls(speed, capacity)

class  Bus(Transport):
    """Класс автобуса, наследующий Transport и хранящий маршрут следования."""

    def __init__(self, destination, speed, capacity):
        """
        Инициализирует экземпляр автобуса.

        :param destination: Словарь вида {номер_маршрута: список_остановок}.
        :param speed: Скорость автобуса.
        :param capacity: Пассажировместимость автобуса.
        """
        super().__init__(speed, capacity)
        self._destination = {}
        self._destination: dict = destination

    def reader(self):
        """Формирует и выводит в консоль маршрут автобуса со всеми остановками."""
        dest = ""
        key = ""

        for key, value in self._destination.items():
            if value:
                dest = PATH_ARROW.join(value)
            else:
                print(f"{self.__class__.__name__}: This destination is empty")

        print(f"\n{self.__class__.__name__}: Route {key} is moving with destination: {dest}")


class Taxi(Transport):
    """Класс такси с расчётом стоимости поездки по тарифу."""

    def __init__(self, speed, capacity, tariff):
        """
        Инициализирует экземпляр такси.

        :param speed: Скорость такси.
        :param capacity: Количество пассажиров.
        :param tariff: Тарифный коэффициент поездки.
        """
        super().__init__(speed, capacity)
        self._tariff = 0
        self._tariff = tariff

    def tariff_value(self):
        """Рассчитывает и выводит стоимость поездки, если пассажиров не больше 4."""
        if self.capacity <= MAX_CAPACITY:
            cost = (self.capacity*BASE_TARIFF_PER_VALUE)*self._tariff
            print(f"\nTaxi tariff cost: {cost}")

class Truck(Transport):
    """Класс грузовика с учётом грузоподъёмности и расчётом стоимости перевозки."""

    def __init__(self, lift_capacity, speed, capacity):
        """
        Инициализирует экземпляр грузовика.

        :param lift_capacity: Максимальная грузоподъёмность.
        :param speed: Скорость грузовика.
        :param capacity: Текущая загрузка (масса груза).
        """
        super().__init__(speed, capacity)
        self._carrying: int = 0
        self._carrying: int= lift_capacity

    def carrying_cost(self):
        """
        Рассчитывает и выводит стоимость перевозки груза при соблюдении лимита грузоподъёмности.

        :return: Итоговая стоимость перевозки или 0 при перегрузе.
        """
        cost_value = 0

        if self._carrying >= self.capacity:
            cost_value += self.capacity * 10 + MANDATORY_TIPS
            print(f"\n{self.__class__.__name__}: Carrying cost - {cost_value}")
        else:
            print(f"\n{self.__class__.__name__}: Too much!")
        return cost_value


if __name__ == "__main__":

#Transport
    obj_0 = Transport(110, 0)
    obj_1 = Transport.from_dict(BASE_DICT)

#Bus
    bus_obj = Bus({"360": STOP_STATIONS}, 110, 30)

#Taxi
    taxi_obj = Taxi(90, 30, 1.25)
    taxi_obj.tariff_value()

#Truck
    truck_obj = Truck(600, 60, 500)
    truck_obj.carrying_cost()

    test_objects = [obj_0, obj_1, bus_obj, taxi_obj,truck_obj]
    for test in test_objects:
        print(test)

    print('\n-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-')

    vehicle_list = [obj_0, obj_1, bus_obj, taxi_obj, truck_obj]

    for vehicle in vehicle_list:
        vehicle.speed_check()


