from functions.get_file_content import *
from functions.get_files_info import *


def main():
    print(get_file_content("calculator", "lorem.txt"))

    print(f"Result for current directory:")
    # print(get_files_info("calculator", "."))
    print(get_file_content("calculator", "main.py"))

    print(f"Result for current directory:")
    # print(get_files_info("calculator", "pkg"))
    print(get_file_content("calculator", "pkg/calculator.py"))

    print(f"Result for '/bin' directory:")
    # print(get_files_info("calculator", "/bin"))
    print(get_file_content("calculator", "/bin/cat"))

    print(f"Result for '../' directory:")
    # print(get_files_info("calculator", "../"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()
