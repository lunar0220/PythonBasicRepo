# ООП 
class BankAccount:
    def __init__(self, deposit: float = 0.0) -> None:
        self.__deposit = deposit
        self.interest_rate = 0.1

    def show_balance(self) -> None:
        print(f"Баланс счета: {self.__deposit}")


    def deposit(self, value: float) -> None:
        self.__deposit += value

    def withdrow(self, value: float) -> None:
        if value > self.__deposit:
            print("ГНевозможно снять данную сумму")
            return 0
        

        self.__deposit -= value
        return value

    @classmethod
    def show_interest_rate(cls) -> None:
        print(f"Процентная ставка: {cls.interest_rate}")


    @staticmethod
    def calculate_result(years_count: int, deposit: float) -> float:
        result = deposit * ((1 + BankAccount.interest_rate) ** years_count)
        return round(result)


class Utils:   #лучше это использовать, не желательно обращаться к строкам из кода выше, а создавать новые
    @staticmethod
    def get_time_now():
        from datetime import datetime
        return datetime.now()


# class Utils:
#     @classmethod
#     def get_time_now(cls):
#         from datetime import datetime
#         return datetime.now()
    

print(BankAccount.calculate_result(100_000, 4))
Utils.get_time_now()
acc_1: BankAccount = BankAccount(100_000) #экзепляр\object
acc_2: BankAccount = BankAccount()
acc_1.show_balance()
acc_1.deposit(25_000)
acc_1.show_balance()
print(acc_1.withdrow(300_000))
acc_1.show_balance()





