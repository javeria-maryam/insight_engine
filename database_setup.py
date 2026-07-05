import sqlite3

def create_database():
    conn = sqlite3.connect("company_data.db")
    cursor = conn.cursor()

    # Create Sales Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
                        id INTEGER PRIMARY KEY,
                        product TEXT,
                        revenue INTEGER,
                        region TEXT,
                        date TEXT)''')

    # Insert Dummy Data
    sales_data = [
        ('Cloud_Storage', 50000, 'Europe', '2026-06-01'),
        ('Cloud_Storage', 45000, 'North America', '2026-06-05'),
        ('Security_Suite', 30000, 'Europe', '2026-06-10'),
        ('Security_Suite', 55000, 'North America', '2026-06-15'),
        ('AI_Consulting', 70000, 'Asia', '2026-06-20')
    ]
    cursor.executemany('INSERT INTO sales (product, revenue, region, date) VALUES (?, ?, ?, ?)', sales_data)
    
    conn.commit()
    conn.close()
    print("Database 'company_data.db' created successfully!")

if __name__ == "__main__":
    create_database()