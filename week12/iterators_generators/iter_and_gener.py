from time import sleep
from os import system, path as osp
from random import choice
from string import ascii_letters
from pynput.mouse import Controller
import subprocess


def chain(iterable_1, iterable_2):
    for el in iterable_1:
        yield el
    for el in iterable_2:
        yield el


def compress(iterable, mask):
    for el_i, el_m in zip(iterable, mask):
        if el_m:
            yield el_i


def cycle(iterable):
    result = ""
    while True:
        for el in iterable:
            result += str(el)
            yield result


def book_reader(file_name=None):
    if file_name:
        with open(file_name, "r") as f:
            this_book = ""
            for el in f.readlines():
                this_book += el
            chapters = this_book.split("#")
            for chapter in chapters:
                yield str(chapter)
                wait_for_press()
        return
    for item in range(1, 100):
        if not osp.exists(str(item).zfill(3) + ".txt"):
            return "The End"
        with open(str(item).zfill(3) + ".txt", "r") as f:
            result = ""
            whole_book = f.readlines()
            for el in whole_book:
                if el[0] == "#":
                    wait_for_press()
                    yield result
                    result = ""
                result += el


def wait_for_press():
    if input("Press any key to continue...") == " ":
        pass
    else:
        wait_for_press()


def book_generator(chapters, chapters_len):
    with open("ObviouslyBook.txt", "w+") as f:
        my_chapter = ""
        for chapter in range(chapters):
            my_chapter += inspirational_quotes(chapters_len)
            f.write(my_chapter)
            wait_for_press()
            yield my_chapter
            my_chapter = ""


def inspirational_quotes(chapters_len):
    result = ""
    for i in range(chapters_len):
        result += choice(ascii_letters + " ")
    return result


def mouse_pointer():
    mouse = Controller()
    print((mouse.position[0], mouse.position[1]))
    if mouse.position[0] < 10 and mouse.position[1] < 10:
        # subprocess.call(['speech-dispatcher'])
        subprocess.call(['spd-say', '"Hack Bulgaria"'])


def main():
    # print(list(chain(range(4), range(4, 8))))
    # print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
    # for item in cycle(range(10)):
    #     print(item)
    # for el in book_reader():
    #     print(el)
    # for el in book_generator(3, 150):
    #     print(el)
    while True:
        mouse_pointer()


if __name__ == "__main__":
    main()
