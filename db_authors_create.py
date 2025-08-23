from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey

engine = create_engine('sqlite:///books.db')
metadata = MetaData()

authors = Table('authors', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(100), nullable=False),
              Column('birth_year', Integer)
)

with engine.connect() as conn:
    # Добавляем авторов
    authors_data = [
        {'name': 'Лев Толстой', 'birth_year': 1828},
        {'name': 'Федор Достоевский', 'birth_year': 1821},
        {'name': 'Антон Чехов', 'birth_year': 1860},
        {'name': 'Александр Пушкин', 'birth_year': 1799},
        {'name': 'Михаил Булгаков', 'birth_year': 1891},
        {'name': 'Иван Тургенев', 'birth_year': 1818},
        {'name': 'Николай Гоголь', 'birth_year': 1809},
    ]
    
    for author in authors_data:
        conn.execute(authors.insert().values(**author))

    conn.commit()
    