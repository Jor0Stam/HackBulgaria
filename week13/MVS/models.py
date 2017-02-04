from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine

from settings import DB_NAME


Base = declarative_base()


class BaseUser(Base):
    __tablename__ = "baseuser"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Student(BaseUser):
    __tablename__ = 'student'
    id = Column(Integer, ForeignKey('baseuser.id'), primary_key=True)
    mac = Column(String(30))
    course = Column(Integer, ForeignKey('course.id'))


def main():
    engine = create_engine(DB_NAME)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
