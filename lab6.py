import sqlite3
def get_records(table_name, field_name):
    # Подключение к базе данных
    conn = sqlite3.connect('bd/goods.db')
    cursor = conn.cursor()

    try:
        query = f"SELECT * FROM {table_name} ORDER BY {field_name}"
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    except sqlite3.Error as e:
        print(f"Ошибка выполнения запроса: {e}")

    finally:
        conn.close()

table_name = "products"
field_name = "product_name"
result = get_records(table_name, field_name)

for record in result:
    print(record)
