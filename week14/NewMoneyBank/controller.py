from model import User, LogLogins
from getpass import getpass
from re import search
from settings import *

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from passlib.hash import pbkdf2_sha256
# pbkdf2_sha256.verify("password", hash) - verify passwords


Base = declarative_base()
engine = create_engine(DB_NAME)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def register():
    username = input("Enter username: ")
    email = input("Enter email: ")
    while email_exists(email):
        email = input("Email exists enter new one!: ")
    add_user(username, get_some_pass(), email)


def email_exists(name):
    try:
        if session.query(User).filter(User.email == name).one():
            return True
    except:
        return False


def get_some_pass():
    password = getpass(GET_PASS)
    repeat_password = getpass("Repeat password: ")
    while (password != repeat_password) or password_not_safe(password):
        if (password != repeat_password):
            print("Passwords must match each other!")
            password = getpass(GET_PASS)
            repeat_password = getpass("Repeat password: ")
        elif password_not_safe(password):
            password = getpass(GET_PASS)
            repeat_password = getpass("Repeat password: ")
    return password


def password_not_safe(password):
    return not(search(r"\d", password) and search(r"[A-Z]", password) and
               search(r"[a-z]", password) and len(password) > 8)


def add_user(new_username, new_password, new_email):
    res = pbkdf2_sha256.encrypt(new_password, rounds=200000, salt_size=16)
    session.add(User(username=new_username, password=res, email=new_email))
    session.commit()


def get_curr_tries(user):
    try:
        usr = session.query(User).filter(User.username == user).one()
    except:
        session.add(LogLogins(id=usr.id, tried=0, time="1"))
        session.commit()
    finally:
        usr = session.query(User).filter(User.username == user).one()
        return session.query(
            LogLogins).filter(
            LogLogins.id == usr.id).one().tried


def add_1_try(curr_tries, usr_id):
    # logOfUsr = session.query(
    # LogLogins).filter(LogLogins.id == usr.id).one()
    session.execute(LogLogins.update(
        LogLogins.tried).where(
        LogLogins.id == usr.id).values(tries=curr_tries + 1))
    session.commit()


def log_try(f):
    def accepter(*args, **kwargs):
        curr_tries = get_curr_tries(args[0])
        # session.add(LogLogins())
    return accepter


@log_try
def login(name, passw):
    users = session.query(User).all()
    for user in users:
        if user.username == name:
            if pbkdf2_sha256.verify(passw, user.password):
                return user
    return False


def send_hash_to_email(user):
    return hash(user.username)


def forgoten_pass(user):
    sended_hash = send_some_hash(user)
    hashed = input(GET_HASH)
    if hashed == sended_hash:
        change_pass(user)
    else:
        print("Incorrect!")


def change_pass(user):
    user.password = get_some_pass()
    session.commit


def main():
    session.add(LogLogins(id=3, tried=1,time="12:00"))
    login("jor0", 123)
    print(get_curr_tries("jor0"))
    add_1_try("jor0", 3)


if __name__ == "__main__":
    main()
