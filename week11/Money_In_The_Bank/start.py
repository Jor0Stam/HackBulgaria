import sql_manager
from re import search
from getpass import getpass
import datetime
from METADATA import *


def main_menu():
    print('''Welcome to our bank service. You are not logged in.
        Please register or login''')

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            while incorrect_password(username, password):
                print("Must contain at least 1 Upper, 1 symbol and 1 digit")
                password = getpass("Enter your password: ")
            sql_manager.register(username, password)

            print("Registration Successfull")

        elif command == 'login':
            if count_user_trying(username) > 5:
                add_user_to_bann_list(username)
            user_login()

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def add_user_to_bann_list(username):
    pass


def count_user_trying(username):
    pass


# def log():
#     def to_log(func):
#         def log_it():
#             with open("logs.py", "a") as f:
#                 f.write(LOG.format(func=func.__name__,
#                                    d_t=datetime.datetime.now()))
#         return log_it
#     return to_log


# @log()
def user_login():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    logged_user = sql_manager.login(username, password)

    if logged_user:
        logged_menu(logged_user)
    else:
        print("Login failed")


def incorrect_password(username, password):
    return not(search(r"\d", password) and search(r"[A-Z]", password) and
               search(r"\W", password) and len(password) > 8 and
               username not in password)


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")

        elif command == "exit":
            raise SystemExit(0)


def main():
    sql_manager.create_tables()
    main_menu()


if __name__ == '__main__':
    main()
