from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import relationship

from settings import DB_NAME

Base = declarative_base()


# class AssociationTable(Base):

#     __tablename__ = "association"
#     id = Column(Integer, primary_key=True)
#     team_id = Column(Integer, ForeignKey('team.id'))
#     skill_id = Column(Integer, ForeignKey('skill.id'))


# child_id = Column(Integer, ForeignKey('child.id'))
# child = relationship("Child", backref="parents")

class Team(Base):

    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    idea_description = Column(String(250), nullable=False)
    technologies_full = Column(Integer, ForeignKey('skill.id'))
    skill = relationship("Skills",
                         backref='team')
    repository = Column(String(250))
    members_needed_desc = Column(String(250))
    room = Column(String(250), nullable=False)
    need_more_members = Column(Boolean)
    place = Column(Integer)


class Skills(Base):

    __tablename__ = "skill"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Mentor(Base):
    __tablename__ = "mentor"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    picture = Column(String(250))
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship('Team',
                           backref='mentor')


# class MentorTeams(Base):

#     __tablename__ = "mentorteams"
#     id = Column(Integer, primary_key=True)
#     team = Column(Integer, ForeignKey("mentor.id"))
#     mentor = Column(Integer, ForeignKey("team.id"))


def main():
    engine = create_engine(DB_NAME)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
