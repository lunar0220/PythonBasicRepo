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
        print(f"Class: {self.grade_class}")
        print()


class Journal:
    def __init__(self) -> None:
        self.__students: list[Student] = []

    def show_students(self) -> None:
        row_index = 1
        for st in self.__students:
            print(f"{row_index}. {st.surname} {st.name} {st.lastname}")
            row_index += 1
        print()

    def add_student(self, st: Student) -> None:
        self.__students.append(st)

    def show_student(self, name: str, surname: str, lastname: str) -> None:
        for st in self.__students:
            if st.name == name and st.surname == surname and st.lastname == lastname:
                st.show_info()
                break

    def del_student(self, name: str, surname: str, lastname: str) -> None:
        ...



journal = Journal()
s_1 = Student(
    name="Ivan",
    surname="Ivanov",
    age=12,
    lastname="Ivanovich",
    grade_class="6 A"
)
s_2 = Student(
    name="Alisa",
    surname="Alisova",
    age=14,
    lastname="Egorovna",
    grade_class="7 B"
)
s_3 = Student(
    name="Egor",
    surname="Antipov",
    age=17,
    lastname="Alexandrovich",
    grade_class="11 C"
)

journal.add_student(s_1)
journal.add_student(s_2)
journal.add_student(s_3)

journal.show_students()

journal.show_student(name="Egor", surname="Antipov", lastname="Alexandrovich")
print(journal.__dict__)

