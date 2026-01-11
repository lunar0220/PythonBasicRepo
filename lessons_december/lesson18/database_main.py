from abstarction.database_manager import DatabaseManager
from abstarction.databases.ch import ClickHouseManager
from abstarction.databases.mssql import MSSQLManager
from abstarction.databases.postgres import PostgresManager


def database_operations(manager: DatabaseManager, conn_str: str, query: str):
    """
    Функция, которая может работать с ЛЮБЫМ объектом,
    который наследует от DatabaseManager (Полиморфизм).
    """
    print("\n" + "="*50)
    manager.connect(conn_str)
    result = manager.execute(query)
    print(f"**Общий лог:** Полученный результат: {result[:30]}...")
    manager.disconnect()
    print("="*50)


def main():
    # Создаем экземпляры конкретных классов
    pg_manager = PostgresManager()
    ms_manager = MSSQLManager()
    ch_manager = ClickHouseManager()
    print("HELLO")
    # Вызываем функцию с разными типами менеджеров, но используем один и тот же интерфейс!
    database_operations(
        pg_manager,
        "user=app dbname=prod_data host=pg.corp",
        "SELECT * FROM users WHERE active = TRUE;"
    )

    database_operations(
        ms_manager,
        "Server=sqlserver\\instance; Database=erp_live",
        "EXECUTE stored_procedure_sales @month='Dec';"
    )

    database_operations(
        ch_manager,
        "http://ch.analytics:8123/cluster",
        "SELECT count() FROM logs_table WHERE event_type='error';"
    )

main()