from jsons import *

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from settings import DB_NAME
from model import Team, Skills, Mentor, MentorTeams


Base = declarative_base()
engine = create_engine(DB_NAME)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# implement it !
def drop_the_base():
    pass


def populate_base():
    Base.metadata.create_all(engine)
    for skill in get_skills():
        session.add(Skills(name=skill["name"]))
    for mentor in get_mentors():
        session.add(Mentor(name=mentor["name"],
                           description=mentor["description"],
                           picture=mentor["picture"],))
    for team in get_teams():
        session.add(Team(name=team["name"],
                         idea_description=team["idea_description"],
                         repository=team["repository"],
                         technologies_full=team["technologies_full"],
                         members_needed_desc=team["members_needed_desc"],
                         room=team["room"],
                         need_more_members=str(team["need_more_members"]),
                         place=0))
    session.commit()


def populate_associate_tables():
    for team in get_teams():
        for skill in team["technologies_full"]:
            session.add(
                TeamSkills(team=session.query(Team).filter(
                    Team.id == team["id"]).all(),
                    skill=skill["id"]))


def main():
    populate_base()


if __name__ == "__main__":
    main()
