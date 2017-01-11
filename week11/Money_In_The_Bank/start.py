import sql_manager
import re


def main_menu():
    print('''Welcome to our bank service. You are not logged in.
        Please register or login''')

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            sql_manager.register(username, password)

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def incorrect_password(password):
    return not(search(r"\d", password) and search(r"[A-Z]", password) and
               search(r"[!, @, #, $, %, ^, &, *,]", password) and len(password) > 7)


def register(mssg=None):
    clear(mssg)
    username = input(USR_INP)
    password = "Not Repeat Password"
    repeat_password = "Not Password!"
    while password != repeat_password or incorrect_password(password):
        password = getpass(PASS_INP)
        repeat_password = getpass(REPEAT_PASS)
        if password != repeat_password:
            register(PASS_ERR)
        if incorrect_password(password):
            register(PASS_INCORECT)
    if not add_user(username, password):
        register(USER_EXIST)
    initiate_HackCinema(USER_CREATED)


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


def main():
    sql_manager.create_clients_table()
    main_menu()


if __name__ == '__main__':
    main()
