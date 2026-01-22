import sqlite3


def main() -> None:
    with ("/Users/anastasiavlasova/Documents/vs code/test_sqlite") as orm:
        data = {
            "name": "TEXT",
            "quantity": "INTEGER",
            "sold": "INTEGER",
        }

        orm.create.table("goods", **data)
        orm.insert("goods", name="Cela", quentity=150, sold=30)
        orm.insert("goods", name="Cheese", quentity=100, sold=89)
        orm.insert("goods", name="Potato", quentity=500, sold=350)
        