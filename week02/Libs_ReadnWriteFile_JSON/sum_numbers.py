import sys
from cat import take_file_info
import re

def sum_content(content):
    content = "".join(content)
    return sum([int(x) for x in re.findall("\d+", content)])

def main():
    with open (sys.argv[1], "r") as f:
        content_to_p = take_file_info(f)
        print(sum_content(content_to_p))

if __name__ == "__main__":
    main()
