from functions.get_file_content import *
from functions.get_files_info import *
from functions.write_file import *


def main():
    # print(get_file_content("calculator", "lorem.txt"))
    # print(f"Result for current directory:")
    # print(get_files_info("calculator", "."))
    # print(get_file_content("calculator", "main.py"))
    # print(f"Result for current directory:")
    # print(get_files_info("calculator", "pkg"))
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print(f"Result for '/bin' directory:")
    # print(get_files_info("calculator", "/bin"))
    # print(get_file_content("calculator", "/bin/cat"))
    # print(f"Result for '../' directory:")
    # print(get_files_info("calculator", "../"))
    # print(get_file_content("calculator", "pkg/does_not_exist.py"))

    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


if __name__ == "__main__":
    main()
