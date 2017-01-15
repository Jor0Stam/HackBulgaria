import sqlite3
from client import Client
from queries import *
from passlib.hash import pbkdf2_sha256


conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def encrypt():
    def accepter(f):
        def encrypting(passwrd):
            hashd = pbkdf2_sha256.encrypt(passwrd, rounds=200000, salt_size=16)
            return hashd
        return encrypting
    return accepter


def create_tables():
    cursor.execute(create_log_table)
    cursor.execute(create_clients_table)


def change_message(new_message, logged_user):
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


@encrypt()
def go_for_password(password):
    return password


def register(username, password):
    cursor.execute(insert_sql, (username, go_for_password(password),))
    conn.commit()


def login(username, password):
    cursor.execute(select_query, (username,))
    user = cursor.fetchone()

    if user and pbkdf2_sha256.verify(password, user[4]):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
