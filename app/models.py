from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Task(Base):
    __table_name__ = "task"

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String, nullable=False)
    date = Column(Date, nullable=False)


class User(Base):
    __table_name__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    mail = Column(String, nullable=False)
    phone = Column(String, nullable=False)
