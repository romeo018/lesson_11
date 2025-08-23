from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import func

engine = create_engine('sqlite:///books.db')
metadata = MetaData()

authors = Table('authors', metadata, autoload_with=engine)
books = Table('books', metadata, autoload_with=engine)

print('=== ЗАДАЧА 1: все авторы ===')

conn = engine.connect()
result = conn.execute(authors.select())

for row in result:
    print(row.name)

# Задача 2: все книги
print('=== ЗАДАЧА 2: все книги ===')

result = conn.execute(books.select())
for row in result:
    print(row.title)
    
# Задача 3: найти Антона Чехова
print('=== Задача 3: найти Антона Чехова ===')

result = conn.execute(authors.select().where(authors.c.name == 'Антон Чехов'))
for row in result:
    print(row)

# ЗАДАЧА 4: НАЙТИ "Война и мир"
print('=== ЗАДАЧА 4: НАЙТИ "Война и мир" ===')

result = conn.execute(books.select().where(books.c.title == 'Война и мир'))
for row in result:
    print(row)
    
# ЗАДАЧА 5: найти книги 1869 года
print('=== ЗАДАЧА 5: найти книги 1869 года ===')   
 
result = conn.execute(books.select().where(books.c.year == 1869))
for row in result:
    print(row)
    
# ЗАДАЧА 6: найти общее количество книг
print('=== ЗАДАЧА 6: найти общее количество книг ===')  
result = conn.execute(select(func.count()).select_from(books))

print(result.scalar())

# ЗАДАЧА 7: сортировка авторов по алфавиту
print('=== ЗАДАЧА 7: сортировка авторов по алфавиту ===')
result = conn.execute(authors.select().order_by(authors.c.name))
for row in result:
    print(row)
    
# ЗАДАЧА 8: найти все книги Льва Толстого
print('=== ЗАДАЧА 8: найти все книги Льва Толстого ===')
result = conn.execute(books.select().join(authors).where(authors.c.name == 'Лев Толстой'))
for row in result:
    print(row)
    
# ЗАДАЧА 9: найти количество книг каждого автора
print('=== ЗАДАЧА 9: найти количество книг по авторам ===')
result = conn.execute(select(authors.c.name, func.count(books.c.id)).join(books).group_by(authors.c.name))
for row in result:
    print(row)