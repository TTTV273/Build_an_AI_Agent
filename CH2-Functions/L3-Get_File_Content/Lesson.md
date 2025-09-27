# Get File Content

Now that we have a function that can get the contents of a directory, we need one that can get the _contents of a file_. Again, we'll just return the file contents as a string, or perhaps an error string if something went wrong.

As always, we'll safely scope the function to a specific working directory.

## Assignment

1. Create a new function in your `functions` directory. Here's the signature I used:

```py
def get_file_content(working_directory, file_path):

```

1. If the `file_path` is outside the `working_directory`, return a string with an error:

```py
f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

```

1. If the `file_path` is not a file, again, return an error string:

```py
f'Error: File not found or is not a regular file: "{file_path}"'

```

1. Read the file and return its contents as a string.  
   * I'll list some useful standard library functions in the `tips` section below.  
   * If the file is longer than `10000` characters, truncate it to `10000` characters and append this message to the end `[...File "{file_path}" truncated at 10000 characters]`.  
   * Instead of hard-coding the `10000` character limit, I stored it in a `config.py` file.

We don't want to accidentally read a gigantic file and send all that data to the LLM... that's a good way to burn through our token limits.

1. If any errors are raised by the standard library functions, catch them and instead return a string describing the error. Always prefix errors with "Error:".
2. Create a new "lorem.txt" file in the `calculator` directory. Fill it with at least 20,000 characters of lorem ipsum text. You can generate some [here](https://www.lipsum.com/).
3. Update your `tests.py` file. Remove all the calls to `get_files_info`, and instead test `get_file_content("calculator", "lorem.txt")`. Ensure that it truncates properly.
4. Remove the lorem ipsum test, and instead test the following cases:  
   * `get_file_content("calculator", "main.py")`  
   * `get_file_content("calculator", "pkg/calculator.py")`  
   * `get_file_content("calculator", "/bin/cat")` (this should return an error string)  
   * `get_file_content("calculator", "pkg/does_not_exist.py")` (this should return an error string)

**Run and submit** the CLI tests.

## Tips

* [os.path.abspath](https://docs.python.org/3/library/os.path.html#os.path.abspath): Get an absolute path from a relative path
* [os.path.join](https://docs.python.org/3/library/os.path.html#os.path.join): Join two paths together safely (handles slashes)
* [.startswith](https://docs.python.org/3/library/stdtypes.html#str.startswith): Check if a string starts with a specific substring
* [os.path.isfile](https://docs.python.org/3/library/os.path.html#os.path.isfile): Check if a path is a file

Example of reading from a file:

```py
MAX_CHARS = 10000

with open(file_path, "r") as f:
    file_content_string = f.read(MAX_CHARS)

```

## Gemini Translation

### **Lấy Nội dung File**

Bây giờ chúng ta đã có một hàm có thể lấy nội dung của một thư mục, chúng ta cần một hàm có thể lấy *nội dung của một file*. Một lần nữa, chúng ta sẽ chỉ trả về nội dung file dưới dạng một chuỗi (string), hoặc có thể là một chuỗi lỗi nếu có sự cố.

Như mọi khi, chúng ta sẽ giới hạn hàm một cách an toàn trong một thư mục làm việc cụ thể.

### **Nhiệm vụ**

1.  Tạo một hàm mới trong thư mục `functions` của bạn. Đây là định nghĩa hàm (signature) tôi đã sử dụng:

    ```py
    def get_file_content(working_directory, file_path):
    ```

2.  Nếu `file_path` nằm ngoài `working_directory`, trả về một chuỗi lỗi:

    ```py
    f'Lỗi: Không thể đọc "{file_path}" vì nó nằm ngoài thư mục làm việc được phép'
    ```

3.  Nếu `file_path` không phài là một file, một lần nữa, trả về một chuỗi lỗi:

    ```py
    f'Lỗi: Không tìm thấy file hoặc đường dẫn không phài là file thông thường: "{file_path}"'
    ```

4.  Đọc file và trả về nội dung của nó dưới dạng chuỗi.

      * Tôi sẽ liệt kê một số hàm thư viện chuẩn hữu ích trong phần `Gợi ý` bên dưới.
      * Nếu file dài hơn `10000` ký tự, hãy cắt ngắn nó còn `10000` ký tự và thêm thông báo này vào cuối `[...File "{file_path}" đã được cắt ngắn ở 10000 ký tự]`.
      * Thay vì gõ trực tiếp (hard-code) giới hạn `10000` ký tự, tôi đã lưu nó trong một file `config.py`.

    > Chúng ta không muốn vô tình đọc một file khổng lồ và gửi tất cả dữ liệu đó đến LLM... đó là một cách tốt để "đốt" hết giới hạn token của chúng ta.

5.  Nếu có bất kỳ lỗi nào được nêu ra bởi các hàm thư viện chuẩn, hãy bắt (catch) chúng và thay vào đó trả về một chuỗi mô tả lỗi. Luôn bắt đầu các lỗi bằng "Lỗi:".

6.  Tạo một file mới tên là "lorem.txt" trong thư mục `calculator`. Điền vào đó ít nhất 20,000 ký tự văn bản lorem ipsum.

7.  Cập nhật file `tests.py` của bạn. Xóa tất cả các lệnh gọi đến `get_files_info`, và thay vào đó kiểm tra `get_file_content("calculator", "lorem.txt")`. Đảm bảo rằng nó cắt ngắn nội dung một cách chính xác.

8.  Xóa bài kiểm tra lorem ipsum, và thay vào đó kiểm tra các trường hợp sau:

      * `get_file_content("calculator", "main.py")`
      * `get_file_content("calculator", "pkg/calculator.py")`
      * `get_file_content("calculator", "/bin/cat")` (trường hợp này nên trả về chuỗi lỗi)
      * `get_file_content("calculator", "pkg/does_not_exist.py")` (trường hợp này nên trả về chuỗi lỗi)

    **Chạy và nộp** bài kiểm tra CLI.

### **Gợi ý**

  * `os.path.abspath`: Lấy đường dẫn tuyệt đối từ một đường dẫn tương đối.
  * `os.path.join`: Nối hai đường dẫn lại với nhau một cách an toàn (xử lý các dấu gạch chéo).
  * `.startswith`: Kiểm tra xem một chuỗi có bắt đầu bằng một chuỗi con cụ thể hay không.
  * `os.path.isfile`: Kiểm tra xem một đường dẫn có phài là file hay không.

Ví dụ về việc đọc từ một file:

```py
MAX_CHARS = 10000

with open(file_path, "r") as f:
    file_content_string = f.read(MAX_CHARS)
```

**Câu hỏi khởi động:** Dựa vào phần `Gợi ý`, bạn sẽ kết hợp `os.path.join` và `os.path.abspath` như thế nào để lấy được đường dẫn tuyệt đối của `file_path` một cách an toàn?
