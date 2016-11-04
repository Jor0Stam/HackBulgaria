import sys


def take_file_info(f):
    return f.readlines()


def format_content(content):
    result = ""
    for i in list(content):
        result += i + "\n"

    return result


def main():
    content_of_file = ""

    with open(sys.argv[1], "r") as f:
        content_to_p = take_file_info(f)
        content_of_file = format_content(content_to_p)

    print(content_of_file)

if __name__ == '__main__':
    main()
