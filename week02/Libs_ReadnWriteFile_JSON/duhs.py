import sys
import os

def get_size(path_to_dir):
    result_size = 0
    for dirpath, dirnames, filenames in os.walk(path_to_dir):
        for f in filenames:
            fpath = os.path.join(dirpath, f)
            result_size += os.path.getsize(fpath)

    return result_size

def main():
    path_to_dir = os.getcwd()
    print(get_size(path_to_dir))


if __name__ == "__main__":
    main()
