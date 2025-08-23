from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey

engine = create_engine('sqlite:///books.db')
metadata = MetaData()

books = Table('books', metadata,
              Column('id', Integer, primary_key=True),
              Column('title', String(200), nullable=False),
              Column('year', Integer),
              Column('author_id', Integer, ForeignKey('authors.id'))
)

with engine.connect() as conn:
    # Добавляем авторов
    books_data = [
        {'title': 'Война и мир', 'year': 1869, 'author_id': 1},
        {'title': 'Анна Каренина', 'year': 1877, 'author_id': 1},
        {'title': 'Преступление и наказание', 'year': 1866, 'author_id': 2},
        {'title': 'Братья Карамазовы', 'year': 1880, 'author_id': 2},
        {'title': 'Вишневый сад', 'year': 1904, 'author_id': 3},
        {'title': 'Евгений Онегин', 'year': 1833, 'author_id': 4},
        {'title': 'Мастер и Маргарита', 'year': 1967, 'author_id': 5},
        {'title': 'Отцы и дети', 'year': 1862, 'author_id': 6},
        {'title': 'Мертвые души', 'year': 1842, 'author_id': 7},
        {'title': 'Ревизор', 'year': 1936, 'author_id': 7}
    ]
    
    for book in books_data:
        conn.execute(books.insert().values(**book))

    conn.commit()
    