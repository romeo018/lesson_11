from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey

engine = create_engine('sqlite:///books.db')
metadata = MetaData()

# Создание таблицы authors
authors = Table('authors', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(100), nullable=False),
              Column('birth_year', Integer)
)

books = Table('books', metadata,
              Column('id', Integer, primary_key=True),
              Column('title', String(200), nullable=False),
              Column('year', Integer),
              Column('author_id', Integer, ForeignKey('authors.id'))
)

metadata.create_all(engine)
