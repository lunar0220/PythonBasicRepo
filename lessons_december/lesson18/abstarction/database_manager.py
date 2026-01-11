from abc import ABC, abstractmethod

# 1. Абстрактный Базовый Класс (АБК) - наш интерфейс
class DatabaseManager(ABC):
    """
    Абстрактный класс, определяющий интерфейс для работы с любой базой данных.
    Каждый конкретный менеджер БД должен реализовать эти методы.
    """

    @abstractmethod
    def connect(self, connection_string: str) -> None:
        """
        Устанавливает соединение с базой данных.
        args:
            - connection_string: str - строка для соединения
        return:
            - None
        """
        pass

    @abstractmethod
    def disconnect(self):
        """Разрывает текущее соединение."""
        pass

    @abstractmethod
    def execute(self, query: str):
        """Выполняет SQL-запрос."""
        pass