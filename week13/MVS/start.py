from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from models import BaseUser
# copy imports from models


def main():
    Base = declarative_base()
    engine = create_engine("sqlite:///Odin.db")
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    baseuser1 = BaseUser(first_name="Az", last_name="VeryAz", password="MayBe")
    baseuser2 = BaseUser(first_name="Ti", last_name="VeryAz", password="MayBe")
    baseuser3 = BaseUser(first_name="Tq", last_name="VeryAz", password="MayBe")
    # session.add(baseuser1)
    # session.commit()

    session.add_all([baseuser1, baseuser2, baseuser3])
    session.commit

    baseusers = session.query(BaseUser).all()
    roza = session.query(BaseUser).filter(BaseUser.first_name == "Az")  # .one() or .all()
    for user in baseusers:
        print(user.first_name)
    # print(roza)


if __name__ == "__main__":
    main()
