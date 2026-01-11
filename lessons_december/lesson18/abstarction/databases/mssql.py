from ..database_manager import DatabaseManager

class MSSQLManager(DatabaseManager):
    """Менеджер для работы с MS SQL Server."""

    def connect(self, connection_string: str):
        # Здесь была бы реальная логика подключения к MSSQL
        print(f"**MSSQL:** Установлено безопасное соединение: {connection_string}")

    def disconnect(self):
        print("**MSSQL:** Соединение с сервером MS SQL закрыто.")

    def execute(self, query: str):
        print(f"**MSSQL:** Отправлен запрос на исполнение: '{query}'")
        return f"Данные, полученные из MSSQL по запросу: {query}"
