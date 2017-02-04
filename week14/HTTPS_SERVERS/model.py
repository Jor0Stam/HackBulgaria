from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import relationship

from settings import DB_NAME

Base = declarative_base()


class AssociationTable(Base):

    __tablename__ = "association"
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('team.id'))
    skill_id = Column(Integer, ForeignKey('skill.id'))


class Team(Base):

    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    idea_description = Column(String(250))
    technologies_full = relationship("Skills",
                                     secondary="association",
                                     back_populates='team')
    repository = Column(String(250))
    members_needed_desc = Column(String(250))
    room = Column(String(250), nullable=False)
    need_more_members = Column(Boolean)
    place = Column(Integer)

    def __str__(self):
        return "{t}".format(t=self.name)

    def __repr__(self):
        return "{t}".format(t=self.name)


class Skills(Base):

    __tablename__ = "skill"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    team = relationship("team",
                        secondary='association',
                        back_populates='skill')


class Mentor(Base):
    __tablename__ = "mentor"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    picture = Column(String(250))
    team_id = Column(Integer, ForeignKey('team.id'))


class MentorTeams(Base):

    __tablename__ = "mentorteams"
    id = Column(Integer, primary_key=True)
    team = Column(Integer, ForeignKey("mentor.id"))
    mentor = Column(Integer, ForeignKey("team.id"))


def main():
    engine = create_engine(DB_NAME)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
