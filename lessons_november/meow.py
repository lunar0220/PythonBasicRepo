class Student:
    def __init__(
            self,
            name: str, 
            surname: str, 
            lastname: str,
            age: int, 
            grade_class: str,
            ) -> None:
        self.name = name
        self.surname = surname
        self.lastname = lastname
        self.age = age
        self.grade_class = grade_class

    def show_info(self) -> None:
        print(f"FIO {self.surname} {self.name} {self.lastname}")
        print(f"Age: {self.age}")
        print(f"Class {self.grade_class}")


class Journal:
    def __init__(self) -> None:
        self.__students: list[Student] = []

    def show_stud(self) -> None:
        row_index = 1
        for st in self.__students:
            print(f"{row_index}. {st.surname} {st.name} {st.lastname}")

    def add_student(self, st: Student) -> None:
        self.__students.append(st)

    def del_student(self, name: str, surname: str, lastname: str) -> None:
        pass

    def show_student(self, name: str, surname: str, lastname: str) -> None:
        for st in self.__students:
            if st.name == name and st.surname == surname and st.lastname == lastname:
                pass

s_1 = Student(
    name="Ivan",
    surname="Ivanov",
    age=12,
    lastname="Ivanovich",
    grade_class="6 A",
)

s_2 = Student(
    name="Anna",
    surname="Ivanova",
    age=18,
    lastname="Vasilieva",
    grade_class="11 A",
)

s_3 = Student(
    name="Sema",
    surname="Petrov",
    age=17,
    lastname="Ivanovich",
    grade_class="10 B",
)

for student in [s_1, s_2, s_3]:
    student.show_info()
    print()
