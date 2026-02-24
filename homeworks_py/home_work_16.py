class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def age(self) -> str:
        return self._age
    

class Employee(Person):
    def __init__(self, name: str, age: int, position: str) -> None:
        super().__init__(name, age)
        self._position = position

    @property
    def position(self) -> str:
        return self._position
    
    def display_info(self) -> None:
        print(f"Employee: {self.name}, Age: {self.age}, Position: {self.position}")
    

class Manager(Employee):
    def __init__(self, name: str, age: int, position: str) -> None:
        super().__init__(name, age, position)
        self._team = []

    def add_to_team(self, employee: Employee) -> None:
        if isinstance(employee, Employee):
            self._team.append(employee)
            print(f"{employee.name} добавлен(а) в команду менеджера {self.name}.")
        else:
            print(f"Ошибка: можно добавлять только сотрудников.")

    def display_team(self) -> None:
        if not self._team:
            print(f"Команда менеджера {self.name} пуста.")
        else:
            print(f"Команда менеджера {self.name}: ")
            for emp in self._team:
                print(f" - {emp.name}, Age: {emp.age}, Position: {emp.position}")


def main():
    employees = []

    while True:
        print("\nВыберете действие:")
        print("1. Добавить нового сотрудника")
        print("2. Добавить нового менеджера")
        print("3. Назначить сотрудника в команду менеджера")
        print("4. Показать всех сотрудников")
        print("5. Показать команду менеджера")
        print("0. Выход")

        choice = input("Введите номер действие: ").strip()

        if choice == "1":
            name = input("Имя сотрудника: ").strip()
            try:
                age = int(input("Возраст сотрудника: ").strip())
            except ValueError:
                print("Ошибка: возраст должен быть числом.")
                continue
            position = input("Должность сотрудника: ").strip()
            emp = Employee(name, age, position)
            employees.append(emp)
            print(f"Сотрудник '{name}' добавлен.")

        elif choice == "2":
            name = input("Имя менеджера: ").strip()
            try:
                age = int(input("Возраст менеджера: ").strip())
            except ValueError:
                print("Ошибка: возраст должен быть числом.")
                continue
            position = input("Должность сотрудника: ").strip()
            mrg = Manager(name, age, position)
            employees.append(mrg)
            print(f"Менеджер '{name}' добавлен.")

        elif choice == '3':
            mgr_name = input("Имя менеджера: ").strip()
            emp_name = input("Введите имя сотрудника: ").strip()

            manager = next((e for e in employees if isinstance(e, Manager) and e.name == mgr_name), None)
            employee = next((e for e in employees if isinstance(e, Employee) and e.name == emp_name), None)

            if not manager:
                print(f"Менеджер '{mgr_name}' не найден.")
            elif not employee:
                print(f"Сотрудник '{emp_name}' не найден.")
            else:
                manager.add_to_team(employee)

        elif choice == "4":
            if not employees:
                print("Сотрудники отсутствуют.")
            else:
                print("Список всех сотрудников:")
                for e in employees:
                    if isinstance(e, Manager):
                        print(f"Manager: {e.name}, Age: {e.age}, Position: {e.position}")
                    else:
                        print(f"Employee: {e.name}, Age: {e.age}, Position: {e.position}")

        elif choice == "5":
            mgr_name = input("Имя менеджера: ").strip()
            manager = next((e for e in employees if isinstance(e, Manager) and e.name == mgr_name), None)
            if manager:
                manager.display_team()
            else:
                print(f"Менеджер '{mgr_name}' не найден.")

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Ошибка: некорректный выбор.")

if __name__ == "__main__":
    main()