import json
import os 
from typing import List, Dict, Any

class Task:
    def __init__(self, title: str, is_done: bool = False) -> None:
        self.title = title
        self.is_done = is_done


    def mark_done(self) -> None:
        self.is_done = True


    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "is_done": self.is_done
        }
    

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Task":
        return Task(data["title"], data["is_done"])
    


class TaskManager:
    def __init__(self, file_name: str = "task.json") -> None:
        self.file_name = file_name
        self.tasks = []
        self.load_from_file()


    def add_task(self, title: str) -> None:
        task = Task(title)
        self.tasks.append(task)
        print(f"Задача '{title}' добавлена.")


    def mark_task_done(self, title: str) -> None:
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                print(f"Задача '{title}' отмечeна как выполненная.")
                return
        print(f"Задача '{title}' не найдена.")


    def show_tasks(self) -> None:
        if not self.tasks:
            print(f"Список задач пуст.")
            return
        
        for index, task in enumerate(self.tasks, start=1):
            status = "Выполнена" if task.is_done else "Не выполнена"
            print(f"{index}. {task.title} - {status}")


    def save_to_file(self) -> None:
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.tasks], file)
        print("Задачи сохранены в файл.")
    

    def load_from_file(self) -> None:
        if os.path.exists(self.file_name):
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]
            print("Задачи загружены из файла.")
        else:
            print("Файл с задачами не найден. Начинаем с пустого списка.")

        
def main() -> None:
    manager = TaskManager()

    while True:
        command = input(f"Введите команду (add, done, show, exit): ").strip().lower()

        if command == "add":
            title = input("Введите название задачи: ").strip()
            manager.add_task(title)

        elif command == "done":
            title = input("Введите название задачи: ").strip()
            manager.mark_task_done(title)

        elif command == "show":
            manager.show_tasks()

        elif command == "exit":
            manager.save_to_file()
            print("Программа завершена.")
            break
        else:
            print("Неизвестная команда. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()