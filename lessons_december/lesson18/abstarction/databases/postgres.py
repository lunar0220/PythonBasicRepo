from ..database_manager import DatabaseManager

class PostgresManager(DatabaseManager):
    """Менеджер для работы с PostgreSQL."""

    def __init__(self):
        self._connection = "sdsad"
        print("-> Инициализирован менеджер PostgreSQL.")

    def connect(self, connection_string: str):
        # Здесь была бы реальная логика подключения к Postgres
        self._connection = f"Postgres Connection: {connection_string}"
        print(f"**Postgres:** Подключено по строке: {connection_string}")

    def disconnect(self):
        if self._connection:
            print("**Postgres:** Соединение разорвано.")
            self._connection = None
        else:
            print("**Postgres:** Соединение уже отсутствует.")

    def execute(self, query: str):
        if self._connection:
            print(f"**Postgres:** Выполнен запрос: '{query}'")
            return f"Результат запроса '{query}' из Postgres"
        else:
            print("**Postgres:** Ошибка! Сначала подключитесь.")
            return None