import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('DROP TABLE IF EXISTS components')
    cursor.execute('''
        CREATE TABLE components (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            name TEXT,
            socket TEXT,
            wattage INTEGER,
            price REAL
        )
    ''')
    
    parts = [
        ('cpu', 'AMD Ryzen 5 7600X', 'AM5', 105, 240.0),
        ('cpu', 'Intel Core i5-13600K', 'LGA1700', 125, 310.0),
        ('mobo', 'MSI PRO B650-P', 'AM5', 0, 190.0),
        ('mobo', 'ASUS Prime Z790', 'LGA1700', 0, 230.0),
        ('psu', '500W Basic', None, 500, 50.0),
        ('psu', '850W Gold', None, 850, 120.0)
    ]
    
    cursor.executemany('INSERT INTO components (category, name, socket, wattage, price) VALUES (?,?,?,?,?)', parts)
    conn.commit()
    conn.close()
    print("Database 'database.db' created successfully.")

if __name__ == "__main__":
    init_db()