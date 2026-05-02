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
            price REAL,
            model TEXT,
            suffix TEXT
        )
    ''')
    parts = [
        ('cpu', 'Intel Core i5-9600K', 'LGA1151', 95, 200.0, 'i5-9600', 'K'),
        ('cpu', 'Intel Core i5-9600KF', 'LGA1151', 95, 190.0, 'i5-9600', 'KF'),
        ('cpu', 'Intel Core i5-9600', 'LGA1151', 65, 180.0, 'i5-9600', ''),
        ('cpu', 'Intel Core i5-9600F', 'LGA1151', 65, 170.0, 'i5-9600', 'F'),
        ('cpu', 'Intel Core i5-13600K', 'LGA1700', 125, 280.0, 'i5-13600', 'K'),
        ('cpu', 'Intel Core i5-13600KF', 'LGA1700', 125, 270.0, 'i5-13600', 'KF'),
        ('cpu', 'Intel Core i9-14900K', 'LGA1700', 253, 550.0, 'i9-14900', 'K'),
        ('cpu', 'Intel Core i9-14900KF', 'LGA1700', 253, 530.0, 'i9-14900', 'KF'),
        ('cpu', 'AMD Ryzen 5 7600X', 'AM5', 105, 210.0, 'Ryzen 5 7600', 'X'),
        ('cpu', 'AMD Ryzen 7 7800X3D', 'AM5', 120, 360.0, 'Ryzen 7 7800', 'X3D'),
        ('mobo', 'MSI Z390-A PRO', 'LGA1151', 0, 130.0, None, None),
        ('mobo', 'Gigabyte Z390 UD', 'LGA1151', 0, 140.0, None, None),
        ('mobo', 'MSI B650 Tomahawk', 'AM5', 0, 190.0, None, None),
        ('mobo', 'ASUS ROG Strix B650-A', 'AM5', 0, 220.0, None, None),
        ('mobo', 'Gigabyte Z790 AORUS ELITE', 'LGA1700', 0, 240.0, None, None),
        ('mobo', 'MSI PRO Z790-P', 'LGA1700', 0, 200.0, None, None),
        ('psu', 'Corsair RM750e 750W', None, 750, 100.0, None, None),
        ('psu', 'Seasonic Focus GX-850 850W', None, 850, 120.0, None, None),
        ('psu', 'be quiet! Pure Power 12 M 1000W', None, 1000, 150.0, None, None)
    ]
    cursor.executemany('INSERT INTO components (category, name, socket, wattage, price, model, suffix) VALUES (?,?,?,?,?,?,?)', parts)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()