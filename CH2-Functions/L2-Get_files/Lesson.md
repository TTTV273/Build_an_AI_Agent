# Get Files

We need to give our agent the ability to _do stuff_. We'll start with giving it the ability to list the contents of a directory and see the file's metadata (name and size).

Before we integrate this function with our LLM agent, let's just build the function itself. Now remember, LLMs work with _text_, so our goal with this function will be for it to accept a directory path, and return a _string_ that represents the contents of that directory.

## Assignment

1. Create a new directory called `functions` in the root of your project (not inside the `calculator` directory). Inside, create a new file called `get_files_info.py`. Inside, write this function:

```py
def get_files_info(working_directory, directory="."):

```

Here is my project structure so far:

```
 project_root/
 ├── calculator/
 │   ├── main.py
 │   ├── pkg/
 │   │   ├── calculator.py
 │   │   └── render.py
 │   └── tests.py
 └── functions/
     └── get_files_info.py

```

The `directory` parameter should be treated as a _relative_ path within the `working_directory`. Use `os.path.join(working_directory, directory)` to create the full path, then validate it stays within the working directory boundaries.

1. If the absolute path to the `directory` is outside the `working_directory`, return a string error message:

```py
f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

```

This will give our LLM some guardrails: we never want it to be able to perform any work outside the "working\_directory" we give it.

Without this restriction, the LLM might go running amok anywhere on the machine, reading sensitive files or overwriting important data. This is a _very_ important step that we'll bake into every function the LLM can call.

1. If the `directory` argument is not a directory, again, return an error string:

```py
f'Error: "{directory}" is not a directory'

```

All of our "tool call" functions, including `get_files_info`, should _always_ return a string. If errors can be raised inside them, we need to catch those errors and return a string describing the error instead. This will allow the LLM to handle the errors gracefully.

1. Build and return a string representing the contents of the directory. It should use this format:

```
- README.md: file_size=1032 bytes, is_dir=False
- src: file_size=128 bytes, is_dir=True
- package.json: file_size=1234 bytes, is_dir=False

```

_I've listed useful standard library functions in the `tips` section_.

The exact file sizes and even the order of files may vary depending on your operating system and file system. Your output doesn't need to match the example byte-for-byte, just the overall format

1. If any errors are raised by the standard library functions, catch them and instead return a string describing the error. Always prefix error strings with "Error:".

To import from a subdirectory, use this syntax: `from DIRNAME.FILENAME import FUNCTION_NAME`

Where `DIRNAME` is the name of the subdirectory, `FILENAME` is the name of the file without the `.py` extension, and `FUNCTION_NAME` is the name of the function you want to import.

1. We need a way to manually debug our new `get_files_info` function! Create a new `tests.py` file in the root of your project. When executed directly (`uv run tests.py`) it should run the following function calls and output the results matching the formatting below (not necessarily the exact numbers).:  
   1. `get_files_info("calculator", ".")`:  
```  
Result for current directory:  
 - main.py: file_size=719 bytes, is_dir=False  
 - tests.py: file_size=1331 bytes, is_dir=False  
 - pkg: file_size=44 bytes, is_dir=True  
```  
   1. `get_files_info("calculator", "pkg")`:  
```  
Result for 'pkg' directory:  
 - calculator.py: file_size=1721 bytes, is_dir=False  
 - render.py: file_size=376 bytes, is_dir=False  
```  
   1. `get_files_info("calculator", "/bin")`:  
```  
Result for '/bin' directory:  
    Error: Cannot list "/bin" as it is outside the permitted working directory  
```  
   1. `get_files_info("calculator", "../")`:  
```  
Result for '../' directory:  
    Error: Cannot list "../" as it is outside the permitted working directory  
```
2. Run `uv run tests.py`, and ensure your function works as expected.

**Run and submit** the CLI tests.

## Tips

Here are some standard library functions you'll find helpful:

* [os.path.abspath()](https://docs.python.org/3/library/os.path.html#os.path.abspath): Get an absolute path from a relative path
* [os.path.join()](https://docs.python.org/3/library/os.path.html#os.path.join): Join two paths together safely (handles slashes)
* [.startswith()](https://docs.python.org/3/library/stdtypes.html#str.startswith): Check if a string starts with a substring
* [os.path.isdir()](https://docs.python.org/3/library/os.path.html#os.path.isdir): Check if a path is a directory
* [os.listdir()](https://docs.python.org/3/library/os.html#os.listdir): List the contents of a directory
* [os.path.getsize()](https://docs.python.org/3/library/os.path.html#os.path.getsize): Get the size of a file
* [os.path.isfile()](https://docs.python.org/3/library/os.path.html#os.path.isfile): Check if a path is a file
* [.join()](https://docs.python.org/3/library/stdtypes.html#str.join): Join a list of strings together with a separator

## Gemini Translation

### Lấy thông tin Tệp

Chúng ta cần cung cấp cho agent của mình khả năng *làm việc*. Chúng ta sẽ bắt đầu bằng cách cho nó khả năng liệt kê nội dung của một thư mục và xem siêu dữ liệu (metadata) của tệp (tên và kích thước).

Trước khi tích hợp hàm này với LLM agent, chúng ta hãy tự xây dựng hàm đó trước. Hãy nhớ rằng, LLM làm việc với *văn bản* (text), vì vậy mục tiêu của chúng ta với hàm này là nó sẽ chấp nhận một đường dẫn thư mục và trả về một *chuỗi* (string) đại diện cho nội dung của thư mục đó.

### Nhiệm vụ

1. Tạo một thư mục mới có tên `functions` ở thư mục gốc của dự án (không phải bên trong thư mục `calculator`). Bên trong, tạo một tệp mới có tên `get_files_info.py`. Viết hàm này bên trong tệp đó:

   ```py
   def get_files_info(working_directory, directory="."):

   ```

   Đây là cấu trúc dự án của tôi cho đến nay:

   ```
    project_root/
    ├── calculator/
    │   ├── main.py
    │   ├── pkg/
    │   │   ├── calculator.py
    │   │   └── render.py
    │   └── tests.py
    └── functions/
        └── get_files_info.py
   ```

   Tham số `directory` nên được coi là một đường dẫn *tương đối* bên trong `working_directory`. Sử dụng `os.path.join(working_directory, directory)` để tạo đường dẫn đầy đủ, sau đó xác thực rằng nó vẫn nằm trong ranh giới của thư mục làm việc.

2. Nếu đường dẫn tuyệt đối đến `directory` nằm ngoài `working_directory`, hãy trả về một chuỗi thông báo lỗi:

   ```py
   f'Lỗi: Không thể liệt kê "{directory}" vì nó nằm ngoài thư mục làm việc được phép'
   ```

   Điều này sẽ cung cấp cho LLM của chúng ta một số rào chắn (guardrails): chúng ta không bao giờ muốn nó có thể thực hiện bất kỳ công việc nào bên ngoài `working_directory` mà chúng ta cung cấp cho nó.

   Nếu không có hạn chế này, LLM có thể chạy lung tung ở bất kỳ đâu trên máy, đọc các tệp nhạy cảm hoặc ghi đè dữ liệu quan trọng. Đây là một bước *rất* quan trọng mà chúng ta sẽ tích hợp vào mọi hàm mà LLM có thể gọi.

3. Nếu tham số `directory` không phải là một thư mục, một lần nữa, hãy trả về một chuỗi lỗi:

   ```py
   f'Lỗi: "{directory}" không phải là một thư mục'
   ```

   Tất cả các hàm "gọi công cụ" (tool call) của chúng ta, bao gồm cả `get_files_info`, phải *luôn* trả về một chuỗi. Nếu có lỗi xảy ra bên trong chúng, chúng ta cần bắt (catch) các lỗi đó và trả về một chuỗi mô tả lỗi thay thế. Điều này sẽ cho phép LLM xử lý các lỗi một cách mượt mà.

4. Xây dựng và trả về một chuỗi đại diện cho nội dung của thư mục. Nó nên sử dụng định dạng này:

   ```
   - README.md: file_size=1032 bytes, is_dir=False
   - src: file_size=128 bytes, is_dir=True
   - package.json: file_size=1234 bytes, is_dir=False
   ```

   *Tôi đã liệt kê các hàm hữu ích từ thư viện chuẩn trong phần `gợi ý`.*

   Kích thước tệp chính xác và ngay cả thứ tự của các tệp có thể thay đổi tùy thuộc vào hệ điều hành và hệ thống tệp của bạn. Đầu ra của bạn không cần phải khớp chính xác từng byte với ví dụ, chỉ cần đúng định dạng chung.

5. Nếu có bất kỳ lỗi nào từ các hàm thư viện chuẩn, hãy bắt chúng và thay vào đó trả về một chuỗi mô tả lỗi. Luôn bắt đầu các chuỗi lỗi bằng "Lỗi:".

6. Chúng ta cần một cách để gỡ lỗi (debug) thủ công hàm `get_files_info` mới của mình! Tạo một tệp `tests.py` mới ở thư mục gốc của dự án. Khi được thực thi trực tiếp (`uv run tests.py`), nó sẽ chạy các lệnh gọi hàm sau và xuất ra kết quả khớp với định dạng bên dưới (không nhất thiết phải là các con số chính xác).

   1. `get_files_info("calculator", ".")`:
      ```
      Kết quả cho thư mục hiện tại:
       - main.py: file_size=719 bytes, is_dir=False
       - tests.py: file_size=1331 bytes, is_dir=False
       - pkg: file_size=44 bytes, is_dir=True
      ```
   2. `get_files_info("calculator", "pkg")`:
      ```
      Kết quả cho thư mục 'pkg':
       - calculator.py: file_size=1721 bytes, is_dir=False
       - render.py: file_size=376 bytes, is_dir=False
      ```
   3. `get_files_info("calculator", "/bin")`:
      ```
      Kết quả cho thư mục '/bin':
          Lỗi: Không thể liệt kê "/bin" vì nó nằm ngoài thư mục làm việc được phép
      ```
   4. `get_files_info("calculator", "../")`:
      ```
      Kết quả cho thư mục '../':
          Lỗi: Không thể liệt kê "../" vì nó nằm ngoài thư mục làm việc được phép
      ```

7. Chạy `uv run tests.py`, và đảm bảo hàm của bạn hoạt động như mong đợi.

**Chạy và nộp** bài kiểm tra CLI.

### Gợi ý

Đây là một số hàm thư viện chuẩn mà bạn sẽ thấy hữu ích:

* [os.path.abspath()](https://docs.python.org/3/library/os.path.html#os.path.abspath): Lấy đường dẫn tuyệt đối từ đường dẫn tương đối
* [os.path.join()](https://docs.python.org/3/library/os.path.html#os.path.join): Nối hai đường dẫn lại với nhau một cách an toàn (xử lý các dấu gạch chéo)
* [.startswith()](https://docs.python.org/3/library/stdtypes.html#str.startswith): Kiểm tra xem một chuỗi có bắt đầu bằng một chuỗi con hay không
* [os.path.isdir()](https://docs.python.org/3/library/os.path.html#os.path.isdir): Kiểm tra xem một đường dẫn có phải là một thư mục hay không
* [os.listdir()](https://docs.python.org/3/library/os.html#os.listdir): Liệt kê nội dung của một thư mục
* [os.path.getsize()](https://docs.python.org/3/library/os.path.html#os.path.getsize): Lấy kích thước của một tệp
* [os.path.isfile()](https://docs.python.org/3/library/os.path.html#os.path.isfile): Kiểm tra xem một đường dẫn có phải là một tệp hay không
* [.join()](https://docs.python.org/3/library/stdtypes.html#str.join): Nối một danh sách các chuỗi lại với nhau bằng một ký tự phân tách

---

Bây giờ khi đã có bản dịch, anh đã sẵn sàng để chúng ta bắt đầu phân tích phần quan trọng nhất - các **yêu cầu về an toàn** - chưa ạ?
