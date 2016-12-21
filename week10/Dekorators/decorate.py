from metadata import *
import datetime
import time


def accepts(*types):
    def func_that_we_use(func):
        def check_acceptance(*info_vars):
            print(types)
            print(info_vars)
            for el1, el2 in zip(types, info_vars):
                if not isinstance(el2, el1):
                    raise TypeError
            return func(*info_vars)
        return check_acceptance
    return func_that_we_use


@accepts(str, int)
def say_hello(name, age):
    return "Hello, I am {} on {}".format(name, age)


def encrypts(key_salad):
    def to_be_encrypted(func):
        def encrypt():
            crypted = ""
            for letter in func():
                if ord(letter) in range(65, 122):
                    crypted += chr(65 + (ord(letter) - 65 + key_salad) % 57)
                else:
                    crypted += letter
            return crypted
        return encrypt
    return to_be_encrypted


def log(where_to_log):
    def to_log(func):
        def log_it():
            with open(where_to_log, "a") as f:
                f.write(LOG.format(func=func.__name__,
                                   d_t=datetime.datetime.now()))
        return log_it
    return to_log


@log("text.txt")
@encrypts(2)
def get_low():
    return "Get get get looow"


def performance(where_to_log):
    def to_log(func):
        def log_it():
            start_time = time.time()
            func()
            with open(where_to_log, "a") as f:
                f.write(PERFORMANCE.format(func=func.__name__,
                                           time=(time.time() - start_time)))
        return log_it
    return to_log


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return "I'm done!"


def main():
    pass
    print(say_hello("Test", 12))
    # print(get_low())
    # something_heavy()


if __name__ == "__main__":
    main()
