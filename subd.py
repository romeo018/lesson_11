# Импорт необходимых библиотек
import sqlite3  # Библиотека для работы с SQLite базами данных
import random   # Библиотека для генерации случайных значений
import string   # Библиотека для работы со строками и символами

# Создание подключения к базе данных
# Если файл database.db не существует, он будет создан автоматически
conn = sqlite3.connect('database.db')

# Создание курсора для выполнения SQL команд
cursor = conn.cursor()

# Создание таблицы users, если она еще не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор, автоматически увеличивается
        username TEXT NOT NULL,                -- Имя пользователя, обязательное поле
        password TEXT NOT NULL                 -- Пароль пользователя, обязательное поле
    )
''')

# Заполнение таблицы случайными данными
# Цикл создает 10 записей пользователей
for i in range(10):
    # Генерация случайного имени пользователя: 'user' + 3 случайные цифры
    username = 'user' + ''.join(random.choices(string.digits, k=3))
    
    # Генерация случайного пароля из 8 символов (буквы и цифры)
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    # Вставка данных в таблицу с использованием параметризованного запроса
    # Знаки ? предотвращают SQL-инъекции
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

# Сохранение всех изменений в базе данных
conn.commit()

# Вывод всех данных из таблицы users
cursor.execute('SELECT * FROM users')  # Выбор всех записей из таблицы
users = cursor.fetchall()              # Получение всех результатов запроса

# Вывод каждого пользователя в консоль
for user in users:
    print(f'ID: {user[0]}, Username: {user[1]}, Password: {user[2]}')

# Закрытие соединения с базой данных
conn.close()