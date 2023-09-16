import sqlite3
import os

# Функция для создания базы данных и таблицы
def create_database():
    # Создаем соединение с базой данных на рабочем столе (или другой папке по вашему выбору)
    db_path = os.path.join(os.path.expanduser("~"), "Desktop", "my_database.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Создаем таблицу с полями: имя, возраст, город
    cursor.execute('''CREATE TABLE IF NOT EXISTS people
                      (name TEXT, age INT, city TEXT)''')

    # Вставляем некоторые данные в таблицу
    cursor.execute("INSERT INTO people VALUES ('Alice', 30, 'New York')")
    cursor.execute("INSERT INTO people VALUES ('Bob', 25, 'Los Angeles')")
    cursor.execute("INSERT INTO people VALUES ('Charlie', 35, 'Chicago')")

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()

# Функция для получения записей по заданному полю
def get_records(table_name, field_name):
    db_path = os.path.join(os.path.expanduser("~"), "Desktop", "my_database.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Выполняем запрос к таблице для выбора записей по заданному полю
    cursor.execute(f"SELECT * FROM {table_name} WHERE {field_name}=?", (field_value,))
    records = cursor.fetchall()

    # Закрываем соединение
    conn.close()

    return records

# Создаем базу данных и таблицу
create_database()

# Задаем имя таблицы и поле для поиска
table_name = "people"
field_name = "age"
field_value = 30

# Получаем записи по заданному полю
result = get_records(table_name, field_name)

# Выводим результат на экран
for record in result:
    print(record)
