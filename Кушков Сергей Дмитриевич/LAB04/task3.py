#/usr/bin/env python3

import random
from abc import ABC, abstractmethod

STANDARD_DELIMITED = ","

class Person:
    """
    Базовый класс, описывающий человека.
    """

    def __init__(self, name, gender, age):
        """
         Инициализирует объект человека с проверкой данных.

        :param name: Имя человека
        :param gender: Пол человека ('М', 'Ж', 'Мужской', 'Женский')
        :param age: Возраст человека (от 0 до 130)
        """
        self.name = name
        self.gender = gender
        self.age = age

    @property
    def name(self):
        """
        Геттер для получения имени человека.

        :return: Имя человека
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Сеттер для имени с проверкой на непустую строку.

        :param value: Новое имя человека
        :raises ValueError: Если имя не строка или пустое
        """
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Имя должно быть непустой строкой!")
        self.__name = value

    @property
    def gender(self):
        """
        Геттер для получения пола человека.

        :return: Пол человека
        """
        return self.__gender

    @gender.setter
    def gender(self, value):
        """
         Сеттер для пола с проверкой допустимых значений.

        :param value: Пол человека
        :raises ValueError: Если передано недопустимое значение пола
        """
        if value not in ["М", "Ж", "Мужской", "Женский"]:
            raise ValueError("Пол должен быть 'М', 'Ж', 'Мужской' или 'Женский'!")
        self.__gender = value

    @property
    def age(self):
        """
        Геттер для получения возраста человека.

        :return: Возраст человека
        """
        return self.__age

    @age.setter
    def age(self, value):
        """
        Сеттер для возраста с проверкой диапазона от 0 до 130 лет.

        :param value: Возраст человека
        :raises ValueError: Если возраст не целое число или вне диапазона
        """
        if not isinstance(value, int) or value < 0 or value > 130:
            raise ValueError("Возраст должен быть целым числом от 0 до 130!")
        self.__age = value

    def get_info(self):
        """
        Возвращает красивую строку с информацией о человеке.

        :return: строка с персональной информацией
        """
        return f"Имя: {self.name}, пол: {self.gender}, возраст: {self.age}"

    def is_adult(self):
        """
        Проверяет, является ли человек совершеннолетним (18+ лет).
        :return: флаг
        """
        return self.age >= 18

    @classmethod
    def from_variables(cls, name, gender, age):
        """
         Классовый метод для конструирования объекта Person через переменные.

        :param name: Имя человека
        :param gender: Пол человека
        :param age: Возраст человека
        :return: Новый экземпляр класса Person
        """
        return cls(name, gender, age)


class Employee(Person, ABC):
    """
    Абстрактный класс сотрудника, наследуемый от Person.
    """

    def __init__(self, name, gender, age, position, salary, monthly_expenses):
        """
        Инициализация сотрудника с вызовом конструктора родителя.

        :param name: Имя сотрудника
        :param gender: Пол сотрудника
        :param age: Возраст сотрудника
        :param position: Должность
        :param salary: Зарплата в месяц
        :param monthly_expenses: Усреднённые расходы в месяц
        """
        super().__init__(name, gender, age)
        self.position = position
        self.salary = salary
        self.monthly_expenses = monthly_expenses
        self.is_alive = True
        self._check_survival()

    @property
    def position(self):
        """
        Геттер для получения должности сотрудника.

        :return: Название должности
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Сеттер для должности с проверкой на пустую строку.

        :param value: Новая должность
        :raises ValueError: Если должность пустая или не строка
        """
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Должность не может быть пустой!")
        self.__position = value

    @property
    def salary(self):
        """
        Геттер для получения зарплаты сотрудника.

        :return: Зарплата сотрудника
        """
        return self.__salary

    @salary.setter
    def salary(self, value):
        """
        Сеттер для зарплаты с проверкой на неотрицательное число.

        :param value: Размер зарплаты
        :raises ValueError: Если зарплата не число или меньше нуля
        """
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Зарплата должна быть положительным числом!")
        self.__salary = value

    @property
    def monthly_expenses(self):
        """
        Геттер для получения ежемесячных расходов.

        :return: Расходы в месяц
        """
        return self.__monthly_expenses

    @monthly_expenses.setter
    def monthly_expenses(self, value):
        """
        Сеттер для расходов с проверкой на неотрицательное число.

        :param value: Размер расходов в месяц
        :raises ValueError: Если расходы не число или меньше нуля
        """
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Расходы должны быть положительным числом!")
        self.__monthly_expenses = value

    def _check_survival(self):
        """
        Проверяет, хватает ли зарплаты на жизнь. Если нет — сотрудник умирает.

        """
        if self.monthly_expenses > self.salary:
            self.is_alive = False
            print(f"{self.name} тратит больше, чем зарабатывает, и умер от голода")

    def get_info(self):
        """
        Переопределяет метод родителя, добавляя должность и финансы.

        """
        parent_info = super().get_info()
        status = "Жив" if self.is_alive else "Мёртв"

        return (f"{parent_info} должность: {self.position}, " 
                f"({status})")

    @abstractmethod
    def work(self):
        """
        Абстрактный метод работы, который должны реализовать наследники.

        """
        pass

    def calculate_cashflow(self, months):
        """
        Считает приток (накопления) денег за N месяцев.

        """
        if not self.is_alive:
            return 0
        if months < 0:
            raise ValueError("Количество месяцев не может быть отрицательным!")
        return (self.salary - self.monthly_expenses) * months

    def calculate_pension_savings(self, retirement_age=65):
        """
        Считает, сколько денег человек скопит до пенсии.

        """
        if not self.is_alive:
            print(f"{self.name} уже умер и не доживёт до пенсии.")
            return 0
        if self.age >= retirement_age:
            print(f"{self.name} уже на пенсии!")
            return 0

        years_left = retirement_age - self.age
        months_left = years_left * 12
        return self.calculate_cashflow(months_left)


class Manager(Employee):
    """
    Класс Менеджера, наследуемый от Employee.

    """

    def __init__(self, name, gender, age, salary, monthly_expenses, subordinates=None):
        """
        Инициализация менеджера и его списка подчинённых.
        :param name: Имя менеджера
        :param gender: Пол менеджера
        :param age: Возраст менеджера
        :param salary: Зарплата
        :param monthly_expenses: Расходы в месяц
        :param subordinates: Начальный список подчинённых (по умолчанию None)
        """
        super().__init__(name, gender, age, "Менеджер", salary, monthly_expenses)
        self.subordinates = list(subordinates) if subordinates else []

    def add_subordinate(self, employee):
        """
        Добавляет подчинённого в список

        """
        if isinstance(employee, Employee):
            self.subordinates.append(employee)
        else:
            raise ValueError("Подчинённым может быть только сотрудник (Employee)!")

    def remove_subordinate(self, employee):
        """
        Удаляет подчинённого из списка

        """
        if employee in self.subordinates:
            self.subordinates.remove(employee)

    def hold_meeting(self):
        """
        Проводит митинг для всех текущих подчинённых

        """
        if not self.is_alive:
            print(f"Менеджер {self.name} не может провести митинг, так как он умер.")
            return
        if not self.subordinates:
            print(f"Менеджер {self.name} хочет провести митинг, но у него нет подчинённых.")
        else:
            print(f"Менеджер {self.name} проводит митинг для")

    def work(self):
        """
        Реализация рабочего процесса менеджера

        """
        if not self.is_alive:
            return f"{self.name} не может работать."
        return f"{self.name} управляет командой ({len(self.subordinates)} чел.) и ставит задачи"

    def get_info(self):
        """
        Переопределение вывода информации с вызовом super()

        """
        base_info = super().get_info()
        return f"{base_info} Подчинённых: {len(self.subordinates)}"


class Developer(Employee):
    """
    Класс Разработчика, наследуемый от Employee

    """

    def __init__(self, name, gender, age, salary, monthly_expenses, languages):
        """
        Инициализация разработчика со списком языков программирования.

        """
        super().__init__(name, gender, age, "Разработчик", salary, monthly_expenses)
        if not isinstance(languages, list) or len(languages) == 0:
            raise ValueError("Список языков программирования не должен быть пустым!")
        self.languages = languages

    def write_code(self):
        """
        Пишет код на случайном языке из своего списка

        """
        if not self.is_alive:
            return f"{self.name} не может кодить."
        chosen_lang = random.choice(self.languages)
        return f"Разработчик {self.name} сейчас пишет код {chosen_lang}."

    def work(self):
        """
        Реализация рабочего процесса разработчика

        """
        return self.write_code()

    def get_info(self):
        """
        Переопределение вывода информации
        """
        base_info = super().get_info()
        langs = STANDARD_DELIMITED.join(self.languages)
        return f"{base_info} Языки: {langs}"


class Designer(Employee):
    """
    Класс Дизайнера, наследуемый от Employee.

    """

    def __init__(self, name, gender, age, salary, monthly_expenses, tools):
        """
        Инициализация дизайнера со списком инструментов
        """
        super().__init__(name, gender, age, "Дизайнер", salary, monthly_expenses)
        if not isinstance(tools, list) or len(tools) == 0:
            raise ValueError("Список инструментов дизайнера не должен быть пустым!")
        self.tools = tools

    def create_mockup(self):
        """
        Создаёт макет с использованием своих инструментов.
        """
        if not self.is_alive:
            return f"{self.name} не может рисовать макеты."
        tool = random.choice(self.tools)
        return f"Дизайнер {self.name} рисует новый макет в программе {tool}"

    def work(self):
        """
        Реализация рабочего процесса дизайнера.

        """
        return self.create_mockup()

    def get_info(self):
        """
        Переопределение вывода информации с вызовом super().

        """
        base_info = super().get_info()
        tools_str = STANDARD_DELIMITED.join(self.tools)
        return f"{base_info} Инструменты: {tools_str}"


if __name__ == "__main__":

    p_name, p_gender, p_age = "Иван", "М", 17
    person1 = Person.from_variables(p_name, p_gender, p_age)
    print(person1.get_info())
    print("Совершеннолетний?", person1.is_adult())


    dev = Developer("Алексей", "М", 25, 150000, 60000, ["Python", "C++", "JavaScript"])
    des = Designer("Мария", "Ж", 28, 120000, 50000, ["Figma", "Photoshop"])
    mgr = Manager("Ольга", "Ж", 35, 180000, 80000)
    poor_dev = Developer("Дмитрий", "М", 22, 50000, 75000, ["PHP"])

    mgr.add_subordinate(dev)
    mgr.add_subordinate(des)
    mgr.hold_meeting()

    employees = [dev, des, mgr, poor_dev]

    for employee_test in employees:
        print(employee_test.get_info())

    for employee_test in employees:

        print(employee_test.work())
        print(f"Приток денег у {dev.name} за 6 месяцев: {dev.calculate_cashflow(6)} руб")
        print(f"Накопления {des.name} до пенсии: {des.calculate_pension_savings()} руб")
        print(f"Накопления {poor_dev.name} до пенсии: {poor_dev.calculate_pension_savings()} руб")
