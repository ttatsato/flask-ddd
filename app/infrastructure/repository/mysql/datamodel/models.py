import sys
import os
from datetime import datetime

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    os.getenv('MYSQL_USER'),
    os.getenv('MYSQL_ROOT_PASSWORD'),
    os.getenv('MYSQL_CONTAINER_NAME'),
    os.getenv('MYSQL_DATABASE')
)

# echo: Trueだと実行するたびにSQLが出力される
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

# Session
# ORM実行時の設定自動コミットするか自動反映するか
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()


class User(Base):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    age = Column('age', Integer)
    email = Column('email', String(100))
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
    modified = Column('modified', DATETIME, default=datetime.now, nullable=False)

    def __init__(self, name: str, age: str, email: str):
        self.name = name
        self.age = age
        self.email = email
        now = datetime.now()
        self.created = now
        self.modified = now


class Dish(Base):
    __tablename__ = "dishes"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    cuisine = Column('cuisine', String(200))
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
    modified = Column('modified', DATETIME, default=datetime.now, nullable=False)

    def __init__(self, name: str, cuisine: str):
        self.name = name
        self.cuisine = cuisine
        now = datetime.now()
        self.created = now
        self.modified = now


def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
