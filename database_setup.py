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
        ('cpu', 'AMD Ryzen 5 7600X', 'AM5', 105, 210.0),
        ('cpu', 'AMD Ryzen 7 7800X3D', 'AM5', 120, 360.0),
        ('cpu', 'Intel Core i5-13600K', 'LGA1700', 125, 280.0),
        ('cpu', 'Intel Core i9-14900K', 'LGA1700', 253, 550.0),
        ('mobo', 'MSI B650 Tomahawk', 'AM5', 0, 190.0),
        ('mobo', 'ASUS ROG Strix B650-A', 'AM5', 0, 220.0),
        ('mobo', 'Gigabyte Z790 AORUS ELITE', 'LGA1700', 0, 240.0),
        ('mobo', 'MSI PRO Z790-P', 'LGA1700', 0, 200.0),
        ('psu', 'Corsair RM750e 750W', None, 750, 100.0),
        ('psu', 'Seasonic Focus GX-850 850W', None, 850, 120.0),
        ('psu', 'be quiet! Pure Power 12 M 1000W', None, 1000, 150.0)
    ]
    
    cursor.executemany('INSERT INTO components (category, name, socket, wattage, price) VALUES (?,?,?,?,?)', parts)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()