#!/usr/bin/env python3



class BankAccount:
    """
    Базовый класс банковского счёта с защитой полей и историей транзакций.
    """
    def __init__(self,balance, holder):
        """
        Инициализирует новый банковский счёт.

        :param balance: Начальный баланс счёта.
        :param holder: Имя владельца счёта.
        """
        if balance < 0:
            raise ValueError("Баланс не может-быть отрицателым")
        self.__balance: float = balance
        self.__holder: str = holder
        self.__history: list[str] = []

    @property
    def history(self):
        """
        Возвращает копию списка истории операций.
        :return: копия списка
        """
        return self.__history.copy()

    @property
    def balance(self):
        """
        Возвращает текущий баланс счёта.
        :return: баланс счёта
        """
        return self.__balance

    @property
    def holder(self):
        """
        Возвращает имя владельца счёта.
        :return: имя владельца
        """
        return self.__holder

    def add_to_balance(self, money):
        """
        Пополняет баланс на указанную сумму и сохраняет операцию в историю.

        :param money: Сумма пополнения
        """
        if isinstance(money, (int, float)):
            if money > 0:
                self.__balance += money
                self.__history.append(f"+{money}")
            else:
                print(f"\nВведите положительное число\n")
        else:
            print("\nВведите число!")

    def withdraw_from_balance(self, money: int | float):
        """
        Снимает указанную сумму со счёта и сохраняет операцию в историю.

        :param money: Суммма списания
        """
        if type(money) in (float,int):
            if money > 0:
                if self.__balance > 0 and self.__balance >= money:
                    self.__balance -= money
                    self.__history.append(f"-{money}")
                else:
                    print(f"На счету не хватает средств!")
            else:
                print(f"Введите положительное число")
        else:
            print("Введите число!")

    @classmethod
    def from_dict(cls, info_dict):
        """
        Создаёт экземпляр банковского счёта из словаря.

        :param info_dict: Словарь с ключами 'balance' и 'holder'.
        :return: Новый объект класса BankAccount.
        """
        balance = info_dict["balance"]
        holder = info_dict["holder"]
        return cls(balance, holder)


class SavingsAccount(BankAccount):
    """
    Сберегательный счёт с начислением процентов и ограничением на снятие.
    """
    def __init__(self, balance, holder, percent):
        """
        Инициализирует сберегательный счёт.

        :param balance: Начальный баланс счёта.
        :param holder: Имя владельца счёта.
        :param percent: Процентная ставка по счёту.
        """
        super().__init__(balance, holder)
        self.__percent: int = percent

    @property
    def percent(self):
        """Возвращает процентную ставку счёта."""
        return self.__percent

    def percent_add(self):
        """
        Начисляет проценты на текущий баланс счёта.
        """
        if isinstance(self.__percent, (int, float)) and 100 >= self.__percent >= 0:
            money = self.balance*(self.__percent / 100)
            super().add_to_balance(money)

    def withdraw_from_balance(self, money: int | float):
        """
        Снимает средства со сберегательного счёта (не более 50% баланса за одну операцию).

        :param money: Сумма снятия.
        """
        if isinstance(money, (int, float)):
            if money > self.balance * 0.5:
                raise ValueError("Со сберегательного счёта нельзя снять более 50% баланса за раз!")
        super().withdraw_from_balance(money)

if __name__ == "__main__":

    personal_data = {"holder":"Sergey", "balance":13000}

    test2 = SavingsAccount(12000, "Andrew", 10)
    test1 = BankAccount.from_dict(personal_data)

    test1.withdraw_from_balance(200)
    test1.add_to_balance(100)
    test1.add_to_balance(-100)
    test2.percent_add()
    test2.withdraw_from_balance(5000)

    print(test1.history)
    print(test1.balance)
    print(test2.history)
    print(test2.balance)

    test_list = [test1, test2]
    for test in test_list:
        test.withdraw_from_balance(3000)
        print(f"\n тест на полифморфизм: {test.balance}, история: {test.history}")

    test2.withdraw_from_balance(4000)



