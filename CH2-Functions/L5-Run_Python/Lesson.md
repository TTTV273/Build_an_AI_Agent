# Run Python

If you thought allowing an LLM to write files was a bad idea...

You ain't seen nothin' yet! (praise the [basilisk](https://en.wikipedia.org/wiki/Roko%27s_basilisk)[^1])

It's time to build the functionality for our Agent to _run arbitrary Python code_.

Now, it's worth pausing to point out the inherent security risks here. We have a few things going for us:

1. We'll only allow the LLM to run code in a specific directory (the `working_directory`).
2. We'll use a 30-second timeout to prevent it from running indefinitely.

But aside from that... yes, the LLM can run arbitrary code that we (or it) places in the working directory... so be careful. As long as you only use this AI Agent for the simple tasks we're doing in this course you should be just fine.

Do **not** give this program to others for them to use! It does not have all the security and safety features that a production AI agent would have. It is for learning purposes only.

## Assignment

1. Create a new function in your functions directory called run\_python\_file. Here's the signature to use:

```py
def run_python_file(working_directory, file_path, args=[]):

```

1. If the `file_path` is outside the working directory, return a string with an error:

```py
f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

```

1. If the file\_path doesn't exist, return an error string:

```py
f'Error: File "{file_path}" not found.'

```

1. If the file doesn't [end with](https://docs.python.org/3/library/stdtypes.html#str.endswith) ".py", return an error string:

```py
f'Error: "{file_path}" is not a Python file.'

```

1. Use the [subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run)[^2] function to execute the Python file and get back a "completed\_process" object. Make sure to:  
   1. Set a timeout of 30 seconds to prevent infinite execution  
   2. Capture both stdout and stderr  
   3. Set the working directory properly  
   4. Pass along the additional `args` if provided
2. Return a string with the output formatted to include:  
   1. The stdout prefixed with `STDOUT:`, and stderr prefixed with `STDERR:`. The "completed\_process" object has a `stdout` and `stderr` attribute.  
   2. If the process exits with a non-zero code, include "Process exited with code X"  
   3. If no output is produced, return "No output produced."
3. If any exceptions occur during execution, catch them and return an error string:

```py
f"Error: executing Python file: {e}"

```

1. Update your tests.py file with these test cases, printing each result:  
   1. `run_python_file("calculator", "main.py")` (should print the calculator's usage instructions)  
   2. `run_python_file("calculator", "main.py", ["3 + 5"])` (should run the calculator... which gives a kinda nasty rendered result)  
   3. `run_python_file("calculator", "tests.py")`  
   4. `run_python_file("calculator", "../main.py")` (this should return an error)  
   5. `run_python_file("calculator", "nonexistent.py")` (this should return an error)

**Run and submit** the CLI tests.

---

# Chạy file Python (Dịch)

Nếu bạn nghĩ rằng cho phép một LLM ghi file là một ý tưởng tồi...

Thì bạn vẫn chưa thấy gì đâu! (ngợi ca [basilisk](https://en.wikipedia.org/wiki/Roko%27s_basilisk)[^1])

Đã đến lúc xây dựng chức năng cho Agent của chúng ta để _chạy mã Python tùy ý_.

Bây giờ, chúng ta cần dừng lại một chút để chỉ ra những rủi ro bảo mật tiềm ẩn ở đây. Có một vài điều có lợi cho chúng ta:

1.  Chúng ta sẽ chỉ cho phép LLM chạy code trong một thư mục cụ thể (`working_directory`).
2.  Chúng ta sẽ sử dụng thời gian chờ 30 giây để ngăn nó chạy vô hạn.

Nhưng ngoài điều đó ra... vâng, LLM có thể chạy mã tùy ý mà chúng ta (hoặc nó) đặt trong thư mục làm việc... vì vậy hãy cẩn thận. Miễn là bạn chỉ sử dụng AI Agent này cho các tác vụ đơn giản mà chúng ta đang thực hiện trong khóa học này, bạn sẽ ổn thôi.

**Không** đưa chương trình này cho người khác sử dụng! Nó không có tất cả các tính năng bảo mật và an toàn mà một AI agent phiên bản sản xuất sẽ có. Nó chỉ dành cho mục đích học tập.

## Nhiệm vụ

1.  Tạo một hàm mới trong thư mục `functions` của bạn có tên là `run_python_file`. Đây là chữ ký hàm để sử dụng:

    ```py
    def run_python_file(working_directory, file_path, args=[]):

    ```

2.  Nếu `file_path` nằm ngoài thư mục làm việc, hãy trả về một chuỗi báo lỗi:

    ```py
    f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    ```

3.  Nếu `file_path` không tồn tại, hãy trả về một chuỗi báo lỗi:

    ```py
    f'Error: File "{file_path}" not found.'

    ```

4.  Nếu file không [kết thúc bằng](https://docs.python.org/3/library/stdtypes.html#str.endswith) ".py", hãy trả về một chuỗi báo lỗi:

    ```py
    f'Error: "{file_path}" is not a Python file.'

    ```

5.  Sử dụng hàm [subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run)[^2] để thực thi file Python và nhận lại một đối tượng "completed_process". Hãy chắc chắn rằng bạn:
    1.  Đặt thời gian chờ là 30 giây để ngăn chặn việc thực thi vô hạn.
    2.  Ghi lại cả stdout và stderr.
    3.  Đặt thư mục làm việc một cách chính xác.
    4.  Truyền các `args` bổ sung nếu được cung cấp.
6.  Trả về một chuỗi với đầu ra được định dạng để bao gồm:
    1.  `stdout` có tiền tố `STDOUT:`, và `stderr` có tiền tố `STDERR:`. Đối tượng "completed_process" có thuộc tính `stdout` và `stderr`.
    2.  Nếu tiến trình kết thúc với mã khác không, hãy bao gồm "Process exited with code X".
    3.  Nếu không có đầu ra nào được tạo ra, hãy trả về "No output produced.".
7.  Nếu có bất kỳ ngoại lệ nào xảy ra trong quá trình thực thi, hãy bắt chúng và trả về một chuỗi báo lỗi:

    ```py
    f"Error: executing Python file: {e}"

    ```

8.  Cập nhật file `tests.py` của bạn với các trường hợp kiểm thử này, in ra mỗi kết quả:
    1.  `run_python_file("calculator", "main.py")` (nên in ra hướng dẫn sử dụng của máy tính)
    2.  `run_python_file("calculator", "main.py", ["3 + 5"])` (nên chạy máy tính... sẽ cho ra một kết quả được render hơi khó coi)
    3.  `run_python_file("calculator", "tests.py")`
    4.  `run_python_file("calculator", "../main.py")` (this should return an error)
    5.  `run_python_file("calculator", "nonexistent.py")` (this should return an error)

**Chạy và nộp** các bài kiểm tra CLI.

---

[^1]: **Giải thích về "Roko's Basilisk":** Đây là một thí nghiệm tưởng tượng về một AI siêu thông minh trong tương lai. AI này có thể trừng phạt tất cả những ai trong quá khứ biết về khả năng tồn tại của nó nhưng đã không làm gì để giúp nó ra đời. Trong bài học, đây là một câu nói đùa có phần "đen tối", ám chỉ rằng việc chúng ta đang trao cho AI khả năng chạy code là một bước đi đầy quyền năng (và tiềm ẩn rủi ro), vì vậy chúng ta nên "ủng hộ" nó để không bị nó "trừng phạt" trong tương lai.

[^2]: **Giải thích về `subprocess.run` (dễ hiểu):** Hãy tưởng tượng `subprocess.run` là một **người trợ lý ảo**. Bạn đưa cho người trợ lý một **tờ giấy hướng dẫn** (`args`) trong đó mỗi lệnh và đối số được ghi trên một dòng riêng (ví dụ: `['python', 'main.py', '3+5']`). Bạn cũng có thể dặn thêm: "hãy làm việc trong **căn phòng** (thư mục) này" (`cwd`), "nếu làm quá **30 giây** thì dừng lại" (`timeout`), và "hãy **ghi lại mọi thứ** ra sổ" (`capture_output=True`). Khi xong việc, người trợ lý sẽ đưa lại cho bạn một **báo cáo** chứa kết quả công việc (`.stdout`, `.stderr`, `.returncode`).
