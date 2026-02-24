import sqlite3

def create_db():
    conn = sqlite3.connect('homeworks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Price REAL NOT NULL,
        Quantity INTEGER NOT NULL
    )
    ''')
    products_to_insert = [
    ('Laptop', 1200.50, 5),
    ('Phone', 800.00, 10),
    ('Tablet', 300.00, 0)
]
    cursor.executemany(
        'INSERT INTO Products (Name, Price, Quantity) VALUES (?, ?, ?)',
        products_to_insert
    )

    cursor.execute(
        'UPDATE Products SET Quantity = 10 WHERE Name = ?',
        ('Laptop',)
    )

    cursor.execute(
        'DELETE FROM Products WHERE Quantity = 0'
    )

    conn.commit()

    cursor.execute('SELECT * FROM Products')
    print(cursor.fetchall())

    conn.close()

create_db()

