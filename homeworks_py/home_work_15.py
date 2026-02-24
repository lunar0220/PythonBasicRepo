class Student:
    students = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.grades = []
        Student.students.append(self)

    def add_grade(self, grade: float) -> None:
        if not Student.is_valid_grade(grade):
            raise ValueError("Оценка должна быть в диапазоне от 1 до 5")
        self.grades.append(grade)

    def average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    @classmethod
    def average_grade_all(cls) -> float:
        if not cls.students:
            return 0.0
        
        total_sum = 0
        total_count = 0

        for students in cls.students:
            total_sum += sum(students.grades)
            total_count += len(students.grades)

        if total_count == 0:
            return 0.0
        
        return total_sum / total_count
    
    @staticmethod
    def is_valid_grade(grade: float) -> bool:
        return 1.0 <= grade <= 5.0
    


def main() -> None:
    students = {}

    while True:
        print("\nВыберете действие:")
        print("1. Добавить нового студента")
        print("2. Добавить оценку студенту")
        print("3. Показать средний балл студента")
        print("4. Показать средний балл всех студентов")
        print("5. Проверить допустимость оценки")
        print("0. Выход")

        choice = input("Ваше действие: ").strip()

        if choice == '1':
            name = input("Введите имя студента: ").strip()
            if name in students:
                print(f"Студент с именем '{name}' уже существует.")
            else:
                students[name] = Student(name)
                print(f"Студент '{name}' добавлен.")

        elif choice == "2":
            name = input("Введите имя студента: ").strip()
            if name not in students:
                print("Студент не найден.")
                continue

            try:
                grade = int(input("Введите оценку: "))
                students[name].add_grade(grade)
                print("Оценка добавлена.")
            except ValueError as error:
                print(f"Ошибка: {error}")

        elif choice == '3':
            name = input("Введите имя студента: ")
            if name not in students:
                print(f"Студент с именем '{name}' не найден.")
                continue
            avg_grade = students[name].average_grade()
            print(f"Средний балл студента '{name}': {avg_grade:.2f}")

        elif choice == '4':
            avg_grade_all = Student.average_grade_all()
            print(f"Средний балл всех студентов: {avg_grade_all:.2f}")

        elif choice == '5':
            grade = int(input("Введите оценку: "))
            if Student.is_valid_grade(grade):
                print("Оценка допустимая")
            else:
                print("Оценка недопустимая")

        elif choice == "0":
            print("Выход из программы")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 5.")


if __name__ == "__main__":
    main()