import sys
import re


def take_file_info(f):
    return f.readlines()


def format_content(content):
    result = ""
    for i in list(content):
        result += i
    return result


def count_chars(content):
    return len(re.findall("[^ \\n]", content))


def count_words(content):
    return len(re.findall("[^ \\n]+", content))


def main():
    with open(sys.argv[1], "r") as f:
        content_to_format = take_file_info(f)
        content_of_file = format_content(content_to_format)
        if sys.argv[2] == 'chars':
            return count_chars(content_of_file)
        elif sys.argv[2] == "words":
            return count_words(content_of_file)
        elif sys.argv[2] == "lines":
            return content_of_file.count('\n')
        else:
            var = sys.argv[2]
            return var + " err404, try with - 'chars', 'words' or 'lines'"


if __name__ == "__main__":
    print(main())
