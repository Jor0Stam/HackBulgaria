from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine

from settings import DB_NAME

Base = declarative_base()


class User(Base):

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)

    def __str__(self):
        return "{u}-{e}".format(u=self.username, e=self.email)

    def __repr__(self):
        return "{u}-{e}".format(u=self.username, e=self.email)


class LogLogins(Base):

    __tablename__ = "log_logins"
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    tried = Column(Integer)
    time = Column(String(250))


def main():
    engine = create_engine(DB_NAME)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
