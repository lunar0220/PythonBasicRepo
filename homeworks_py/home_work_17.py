from datetime import datetime
from typing import Callable

def log_action(action: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{current_time}] Выполняется: {action}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.undo_tasks = []

    @log_action("Add Task")
    def add_tasks(self, tasks: str) -> None:
        self.tasks.append(tasks)
        print(f"Задача добавлена")

    @log_action("Show Tasks")
    def show_tasks(self) -> None:
        if not self.tasks:
            print(f"Список задач пуст")
            return
        
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    @log_action("Complete Task")
    def complete_task(self, index: int) -> None:
        if not self.tasks:
            print(f"Список задач пуст")
            return
        
        if index < 1 or index > len(self.tasks):
            print(f"Некорректный номер задачи")
            return
        completed_task = self.tasks.pop(index - 1)
        self.undo_tasks.append(completed_task)
        print(f"Задача '{completed_task}' выполнена")

    @log_action("Undo Task")
    def undo_task(self) -> None:
        if not self.undo_tasks:
            print(f"Нет задач для отмены")
            return
        
        task = self.undo_tasks.pop()
        self.tasks.append(task)
        print(f"Задача '{task}' возращена в список задач")
        

    def run(self) -> None:
        while True:
            command = input("\nВведите команду (add, show, complete, undo, exit): ").strip().lower()
            if command == "add":
                task = input("Введите задачу: ").strip()
                if task:
                    self.add_tasks(task)
                else:
                    print(f"Задача не может быть пустой")

            elif command == "show":
                self.show_tasks()
            elif command == "complete":
                try:
                    index = int(input("Введите номер задачи для выполнения: ").strip())
                    self.complete_task(index)
                except ValueError:
                    print(f"Некорректный ввод. Введите номер задачи.")
            elif command == "undo":
                self.undo_task()
            elif command == "exit":
                print(f"Выход из программы.")
                break
            else:
                print(f"Неизвестная команда")

if __name__ == "__main__":
    manager = TaskManager()
    manager.run()