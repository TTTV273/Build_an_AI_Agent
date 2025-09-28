# Write File

Up until now our program has been read-only... now it's getting _really_ ~~dangerous~~ fun! We'll give our agent the ability to write and overwrite files.

## Assignment

1. Create a new function in your `functions` directory. Here's the signature I used:

```py
def write_file(working_directory, file_path, content):

```

1. If the `file_path` is outside of the `working_directory`, return a string with an error:

```py
f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

```

1. If the `file_path` doesn't exist, create it. As always, if there are errors, return a string representing the error, prefixed with "Error:".
2. Overwrite the contents of the file with the `content` argument.
3. If successful, return a string with the message:

```py
f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

```

It's important to return a success string so that our LLM knows that the action it took actually worked. Feedback loops, feedback loops, feedback loops!

1. Remove your old tests from `tests.py` and add three new ones, as always print the results of each:  
   * `write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")`  
   * `write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")`  
   * `write_file("calculator", "/tmp/temp.txt", "this should not be allowed")`

**Run and submit** the CLI tests.

## Tips

* [os.path.exists](https://docs.python.org/3/library/os.path.html#os.path.exists): Check if a path exists
* [os.makedirs](https://docs.python.org/3/library/os.html#os.makedirs): Create a directory and all its parents
* [os.path.dirname](https://docs.python.org/3/library/os.path.html#os.path.dirname): Return the directory name

Example of writing to a file:

```py
with open(file_path, "w") as f:
    f.write(content)

```

---
# Ghi File (Dịch)

Từ trước đến nay, chương trình của chúng ta chỉ có quyền đọc... bây giờ nó sẽ trở nên _thực sự_ ~~nguy hiểm~~ thú vị! Chúng ta sẽ cung cấp cho agent của mình khả năng ghi và ghi đè lên các file.

## Nhiệm vụ

1.  Tạo một hàm mới trong thư mục `functions` của bạn. Đây là chữ ký hàm tôi đã sử dụng:

    ```py
    def write_file(working_directory, file_path, content):

    ```

2.  Nếu `file_path` nằm ngoài `working_directory` được phép, hãy trả về một chuỗi báo lỗi:

    ```py
    f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    ```

3.  Nếu `file_path` không tồn tại, hãy tạo nó. Như thường lệ, nếu có lỗi, hãy trả về một chuỗi biểu thị lỗi, có tiền tố "Error:".
4.  Ghi đè nội dung của file bằng đối số `content`.
5.  Nếu thành công, trả về một chuỗi với thông báo:

    ```py
    f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    ```

    Điều quan trọng là phải trả về một chuỗi thành công để LLM của chúng ta biết rằng hành động nó thực hiện đã thực sự hiệu quả. Vòng lặp phản hồi, vòng lặp phản hồi, vòng lặp phản hồi!

6.  Xóa các bài kiểm tra cũ của bạn khỏi `tests.py` và thêm ba bài mới, như thường lệ, hãy in kết quả của mỗi bài:
    *   `write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")`
    *   `write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")`
    *   `write_file("calculator", "/tmp/temp.txt", "this should not be allowed")`

**Chạy và nộp** các bài kiểm tra CLI.

## Gợi ý

*   [os.path.exists](https://docs.python.org/3/library/os.path.html#os.path.exists): Kiểm tra xem một đường dẫn có tồn tại không
*   [os.makedirs](https://docs.python.org/3/library/os.html#os.makedirs): Tạo một thư mục và tất cả các thư mục cha của nó
*   [os.path.dirname](https://docs.python.org/3/library/os.path.html#os.path.dirname): Trả về tên thư mục

Ví dụ về cách ghi vào file:

```py
with open(file_path, "w") as f:
    f.write(content)

```