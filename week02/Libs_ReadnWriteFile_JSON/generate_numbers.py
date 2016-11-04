import sys
import os
from random import randint
from cat import take_file_info
from cat import format_content


def fill_it(f, num):
    for i in range(int(num)):
        f.write(str(randint(1, int(num))) + " ")


def main():
    with open(sys.argv[1], "w+") as f:
        fill_it(f, sys.argv[2])

    with open(sys.argv[1], "r") as f:
        content_to_p = take_file_info(f)
        print(format_content(content_to_p))

if __name__ == '__main__':
    main()
