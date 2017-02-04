from controller import *
from subprocess import call


def clear_screen(mssg=False):
    call("clear")
    if mssg:
        print(mssg)


def log_menu():
    while True:
        clear_screen(WELCOME_MSSG)
        command = input("$$$>")

        if command == 'register':
            register()
            print("Registration Successfull")

        elif command == 'log in':
            user = input("Username: ")
            passw = getpass("Password: ")
            main_menu(login(user, passw))

        elif command == 'help':
            print("log in - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command!")


def main_menu(curr_user):
    clear_screen("Welcome {}".format(curr_user.username))

    while True:
        command = input("\nLogged>>")

        if command == 'info':
            print(curr_user)

        elif command == 'forgotpass':
            forgoten_pass(curr_user)

        elif command == 'help':
            print('''info - for showing account info")
forgotpass - for changing passowrd''')

        elif command == "exit":
            SystemExit(0)
        else:
            print("Not a valid command!")


def main():
    log_menu()


if __name__ == "__main__":
    main()
