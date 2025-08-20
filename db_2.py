# Импорт всех функций и классов из SQLAlchemy
from sqlalchemy import *
# Дополнительный импорт MetaData для работы с метаданными таблиц
from sqlalchemy import MetaData

# Создание движка базы данных SQLite
# Строка подключения указывает на файл database.db в текущей директории
engine = create_engine('sqlite:///database.db')

# Создание объекта MetaData для хранения информации о структуре таблиц
metadata = MetaData()

# Создание объекта Table, который автоматически загружает структуру таблицы 'users'
# autoload_with=engine означает, что структура будет загружена из существующей БД
users = Table('users', metadata, autoload_with=engine)

# Установка соединения с базой данных
conn = engine.connect() 

# Выполнение SQL запроса SELECT для получения всех записей из таблицы users
# select(users) создает запрос "SELECT * FROM users"
result = conn.execute(select(users))

# Получение всех результатов запроса в виде списка кортежей
all_users = result.fetchall()

# Вывод всех пользователей в консоль, каждый с новой строки
# * распаковывает список, sep='\n' разделяет элементы переносом строки
print(*all_users, sep='\n')