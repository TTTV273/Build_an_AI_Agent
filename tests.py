from functions.get_file_content import *
from functions.get_files_info import *
from functions.run_python_file import *
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

    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))


if __name__ == "__main__":
    main()
