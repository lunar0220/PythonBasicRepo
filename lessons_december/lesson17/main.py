class BankAccount:
    interest_rate = 0.1

    def __init__(self, deposit: float = 0) -> None:
        self.__deposit = deposit

    def show_balance(self) -> None:
        print(f"Баланс счета: {self.__deposit}")

    def deposit(self, value: float) -> None:
        self.__deposit += value

    def withdraw(self, value: float) -> float:
        if value > self.__deposit:
            print("Невозможно снять данную сумму")
            return 0
        
        self.__deposit -= value
        return value
    
    @classmethod
    def show_interest_rate(cls) -> None:
        print(f"Процентная ставка: {cls.interest_rate}")

    @staticmethod
    def calculate_result(deposit: float, years_count: int, interest_rate: float) -> float:
        result = deposit * ((1 + interest_rate) ** years_count)
        return round(result, 2)
    

    
# Inheritance
class Animal:
    def __init__(self, sound: str) -> None:
        self.sound = sound

    def speak(self) -> None:
        print(f"{self.sound}-{self.sound}...")

    def run(self) -> None:
        print("Running...")

    def show_info(self):
        for key, val in self.__dict__.items():
            print(f"{key} - {val}")
        print()

class Dog(Animal):
    def __init__(self, sound: str, name: str) -> None:
        self.name = name
        super().__init__(sound)

    def hunt(self) -> None:
        print("Hunting....")

class Cat(Animal):
    def __init__(self, sound: str, type: str) -> None:
        self.type = type
        super().__init__(sound)

    def pur_pur(self) -> None:
        print("мрмрмрмрмр")


class Figure:
    def __init__(self, name: str) -> None:
        self.name = name

class Rectangle(Figure):
    def __init__(self, name: str, length: float, width: float) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self) -> float:
        return self.length * self.width
    
class Square:
    def __init__(self, name: str, length: float) -> None:
        self.rect = Rectangle(name, length, length)
        self.fig = Figure(name)

    def area(self) -> float:
        return self.rect.area()
    

class DataBase:
    def connect():
        '''
        Connect with db
        '''
        pass

    def disconnect():
        pass

    def load():
        pass


class Postgres(DataBase):
    def connect():
        pass

    def disconnect():
        pass

    def load():
        pass

class MSSQL(DataBase):
    def connect():
        pass

    def disconnect():
        pass

    def load():
        pass

class MYSQL(DataBase):
    def connect():
        pass

    def disconnect():
        pass

    def load():
        pass


sq = Square("square", length=10)
print(sq.area())


