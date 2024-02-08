import tkinter as tk
import sqlite3


def show_people():
    try:
        result = c.execute("SELECT first_name, last_name, age FROM people").fetchall()
        for idx, (first_name, last_name, age) in enumerate(result):
            label = tk.Label(root, text=f"{idx + 1}. {first_name} {last_name}, возраст: {age}")
            label.pack()
    except Exception as e:
        print(f"An error occurred: {e}")


# Создание базы данных и таблицы, если они не существуют
try:
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS people
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  first_name TEXT NOT NULL,
                  last_name TEXT NOT NULL,
                  age INTEGER NOT NULL)''')
    conn.commit()

    # Вставка данных из словаря в базу данных (выполнить только при первом запуске программы)
    initial_data = [
        ('Алексей', 'Смирнов', 40),
        ('Елена', 'Иванова', 35),
        ('Дмитрий', 'Петров', 29),
        ('Ольга', 'Сидорова', 42),
        ('Сергей', 'Кузнецов', 38),
        ('Анна', 'Васильева', 27),
        ('Михаил', 'Попов', 33),
        ('Татьяна', 'Соколова', 31),
        ('Андрей', 'Михайлов', 45),
        ('Юлия', 'Новикова', 36)
    ]

    c.executemany('INSERT INTO people (first_name, last_name, age) VALUES (?, ?, ?)', initial_data)
    conn.commit()
except Exception as e:
    print(f"An error occurred: {e}")

# Создание графического интерфейса с помощью Tkinter
root = tk.Tk()
root.title("Список людей")

# Создание функции для получения и отображения данных из базы данных

# Вызов функции для отображения данных
show_people()

root.mainloop()
