from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine


Base = declarative_base()


class Server(Base):

    __tablename__ = "server"
    id = Column(Integer, primary_key=True)
    server = Column(String(250), nullable=False)
    times_used = Column(Integer)


def main():
    engine = create_engine("sqlite:///CrawledServers.db")
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
