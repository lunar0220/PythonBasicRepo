from __future__ import annotations
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
import json


PRIORITIES = {"низкий", "средний", "высокий"}
STATUSES = {"новый", "в работе", "завершен"}
CATEGORIES = {"дом", "здоровье", "учеба"}  


class Task:
    """Класс для управления задачами."""
    def __init__(self, task_id: int, title: str, description: str, priority: str, date_due: datetime) -> None:
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = self._validate_priority(priority)
        self.status = "новый"
        self.date_created = datetime.now()
        self.date_due = date_due
    
    @staticmethod
    def _validate_priority(priority: str) -> str:
        """Проверяет допустимый приоритет."""
        if priority not in PRIORITIES:
            raise ValueError(f"Недопустимый приоритет: {priority}")
        return priority
    
    def set_status(self, status: str) -> None:
        """Устанавливает статус задачи."""
        if status not in STATUSES:
            raise ValueError(f"Недопустимый статус: {status}")
        self.status = status

    def is_overdue(self) -> bool:
        """Проверяетб просрочена ли задача."""
        return datetime.now() > self.date_due and self.status != "завершен"
    
    def to_dict(self) -> Dict[str, Any]:
        """Возвращает представление задачи в виде словаря."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "date_created": self.date_created.isoformat(),
            "date_due": self.date_due.isoformat() 
        }
    
    def __repr__(self) -> str:
        """Строковое представление задачи."""
        return f"Task({self.task_id}, {self.title}, {self.priority}, {self.status})"
    

class PersonalTask(Task):
    """Класс для личных задач."""
    def __init__(self, task_id: int, title: str, description: str, priority: str, date_due: datetime, category: str) -> None:
        super().__init__(task_id, title, description, priority, date_due)
        self.category = self._validate_category(category)
    
    @staticmethod
    def _validate_category(category: str) -> str:
        """Проверяет допустимую категорию."""
        if category not in CATEGORIES:
            raise ValueError(f"Недопустимая категория: {category}")
        return category
    
    def to_dict(self) -> Dict[str, Any]:
        """Возвращает представление задачи в виде словаря."""
        data = super().to_dict()
        data["type"] = "PersonalTask"
        return data


class WorkTask(Task):
    """Класс для рабочих задач."""
    def __init__(self, task_id: int, title: str, description: str, priority: str, date_due: datetime, project: str, responsible: str) -> None:
        super().__init__(task_id, title, description, priority, date_due)
        self.project = project
        self.responsible = responsible

    def to_dict(self) -> Dict[str, Any]:
        """Возвращает представление задачи в виде словаря."""
        data = super().to_dict()
        data["project"] = self.project
        data["type"] = "WorkTask"
        return data
    

class TaskManager:
    """Класс для управления коллекцией задач."""
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Добавляет новую задачу."""
        if any(t.task_id == task.task_id for t in self.tasks):
            raise ValueError(f"Задача с ID {task.task_id} уже существует.")
        self.tasks.append(task)

    def remove_task(self, task_id: int) -> None:
        """Удаляет задачу по её ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return
        raise ValueError(f"Задача с ID {task_id} не найдена.")

    def update_status(self, task_id: int, new_status: str) -> None:
        """Обновляет статус задачи по её ID."""
        task = self.get_tasks_by_id(task_id)
        task.set_status(new_status)
    
    def get_tasks_by_id(self, task_id: int) -> Task:
        """Возвращает задачу по её ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        raise ValueError(f"Задача с ID {task_id} не найдена.")
    
    def get_tasks_by_priority(self, priority: str) -> List[Task]:
        """Возвращает задачи с заданным приоритетом."""
        return [task for task in self.tasks if task.priority == priority]
    
    def get_tasks_by_status(self, status: str) -> List[Task]:
        """Возвращает задачи с заданным статусом."""
        return [task for task in self.tasks if task.status == status]
    
    def get_overdue_tasks(self) -> List[Task]:
        """Возвращает просроченные задачи."""
        return [task for task in self.tasks if task.is_overdue()]
    
    def get_tasks_due_soon(self, days: int) -> List[Task]:
        """Возвращает задачи, срок выполнения которых истекает в ближайшие 'days' дней."""
        limit = datetime.now() + timedelta(days=days)
        return [task for task in self.tasks if task.date_due <= limit and task.status != "завершен"]
    
    
    def sort_by_priority(self) -> List[Task]:
        priority_order = {"низкий": 1, "средний": 2, "высокий": 3}
        return sorted(self.tasks, key=lambda t: priority_order[t.priority], reverse=True)

    def sort_by_due_date(self) -> List[Task]:
        return sorted(self.tasks, key=lambda t: t.date_due)

    def sort_by_date_created(self) -> List[Task]:
        return sorted(self.tasks, key=lambda t: t.date_created)

    def export_to_json(self, file_path: str) -> None:
        """Экспортирует задачи в JSON."""
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=4)

    

class TaskFilter:
    """Класс для фильтрации задач по различным критериям."""
    def __init__(self, tasks: List[Task]) -> None:
        self.tasks = tasks

    def filter_by_date_range(self, start_date: datetime, end_date: datetime) -> List[Task]:
        """Фильтрует задачи по диапазону дат."""
        return [task for task in self.tasks if start_date <= task.date_due <= end_date]
    
    def filter_by_multiple_criteria(self, priority: Optional[str] = None, status: Optional[str] = None, category: Optional[str] = None) -> List[Task]:
        """Фильтрует задачи по нескольким критериям."""
        result = self.tasks
        if priority:
            result = [task for task in result if task.priority == priority]
        if status:
            result = [task for task in result if task.status == status]
        if category:
            result = [task for task in result if isinstance(task, PersonalTask) and task.category == category]
        return result


if __name__ == "__main__":
    manager = TaskManager()

    task1 = PersonalTask(1, "Купить продукты", "Молоко и хлеб", "средний", datetime.now() + timedelta(days=2), "дом")

    task2 = WorkTask(2, "Отчет по проекту", "Подготовить отчет", "высокий", datetime.now() + timedelta(days=1), "Проект А", "Иванов И.И.")

    manager.add_task(task1)
    manager.add_task(task2)

    manager.update_status(1, "в работе")

    print("Высокий приоритет:", manager.get_tasks_by_priority("высокий"))
    print("Просроченные задачи:", manager.get_overdue_tasks())
    print("Скоро дедлайн:", manager.get_tasks_due_soon(3))

    task_filter = TaskFilter(manager.sort_by_due_date())
    print("Категория 'дом':",
          task_filter.filter_by_multiple_criteria(category="дом"))

    manager.export_to_json("tasks.json")