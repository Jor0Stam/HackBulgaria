import sys
from cat import format_content

def take_file_info(f):
    return f.readlines()


def main():
    for i in range(1, len(sys.argv)):
        with open(sys.argv[i], "r") as f:
            content_to_p = take_file_info(f)
            content_of_file = format_content(content_to_p)
            print(content_of_file + '\n')

if __name__ == '__main__':
    main()
