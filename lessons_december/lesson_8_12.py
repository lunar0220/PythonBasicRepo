# # OOП - существуют и обьекты и классы
# основные парадигмы:
# # -инкапсуляция
# # -наследование
# # -полиформизм
# # -абстракция

# print(type(10))

# a: list[int] = [10, 20, 100]
# a.append(10)


class Auto:
    def __init__(self, name: str, horse_power: int, speed: int) -> None:
        self.__name = name
        self.__horse_pow = horse_power
        self.__speed = speed

    def __str__(self) -> str:
        return f"Обьект класса Auto {self.name}"

    @property #гетр
    def speed(self) -> None:
        return self.__speed
    

    @speed.setter
    def speed(self, value: int) -> None:
        self.__speed = value               #сетр


    @property 
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, val: int) -> None:
        self.__name = val

    
    @property 
    def horse_pow(self) -> str:
        return self.__horse_pow
    
    @horse_pow.setter
    def horse_pow(self, val: int) -> None:
        self.__horse_pow = val


    def get_info(self) -> None:
        print(f"Model: {self.name}")
        print(f"Max speed: {self.max_speed}")


    def calculate_time(self, length: float) -> None:
        return length / self.speed


    def calculate_length(self, time: float) -> None:
        return self.speed * time
    
bmw: Auto = Auto("BMW", 300, 120)
lada: Auto = Auto("LADA", 160, 90)

print(bmw.calculate_time(300), lada.calculate_time(300))
print(bmw.calculate_length(3), lada.calculate_length(3))
# bmw.get_info   =    Auto.get_info()


