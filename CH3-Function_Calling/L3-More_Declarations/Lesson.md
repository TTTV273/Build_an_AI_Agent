# More Declarations

Now that our LLM is able to specify a function call to the `get_files_info` function, let's give it the ability to call the other functions as well.

## Assignment

1. Following the same pattern that we used for `schema_get_files_info`, create function declarations for:
   * `schema_get_file_content`
   * `schema_run_python_file`
   * `schema_write_file`
2. Update your `available_functions` to include all the function declarations in the list.
3. Update your system prompt. Instead of the allowed operations only being:

```
- List files and directories

```

Update it to have all four operations:

```
- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

```

4. Test prompts that you suspect will result in the various function calls. For example:
   * "read the contents of main.py" -> `get_file_content({'file_path': 'main.py'})`
   * "write 'hello' to main.txt" -> `write_file({'file_path': 'main.txt', 'content': 'hello'})`
   * "run main.py" -> `run_python_file({'file_path': 'main.py'})`
   * "list the contents of the pkg directory" -> `get_files_info({'directory': 'pkg'})`

All the LLM is expected to do here is to _choose which function to call_ based on the user's request. We'll have it _actually call_ the function later.

**Run and submit** the CLI tests.

---

## Gemini Translation

# Thêm Nhiều Khai Báo Hàm

Bây giờ LLM của chúng ta đã có khả năng chỉ định lời gọi hàm (function call) đến hàm `get_files_info`, hãy cho nó khả năng gọi các hàm khác nữa.

## Nhiệm vụ

1. Theo cùng pattern (mẫu) mà chúng ta đã sử dụng cho `schema_get_files_info`, hãy tạo các khai báo hàm (function declarations) cho:
   * `schema_get_file_content`
   * `schema_run_python_file`
   * `schema_write_file`

2. Cập nhật `available_functions` của bạn để bao gồm tất cả các khai báo hàm trong danh sách.

3. Cập nhật system prompt của bạn. Thay vì các phép toán được phép chỉ là:

```
- List files and directories
```

Hãy cập nhật để có đầy đủ bốn phép toán:

```
- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files
```

4. Kiểm tra các prompt (câu lệnh) mà bạn nghi ngờ sẽ dẫn đến các lời gọi hàm khác nhau. Ví dụ:
   * "read the contents of main.py" -> `get_file_content({'file_path': 'main.py'})`
   * "write 'hello' to main.txt" -> `write_file({'file_path': 'main.txt', 'content': 'hello'})`
   * "run main.py" -> `run_python_file({'file_path': 'main.py'})`
   * "list the contents of the pkg directory" -> `get_files_info({'directory': 'pkg'})`

Tất cả những gì LLM được kỳ vọng làm ở đây là _chọn hàm nào để gọi_ dựa trên yêu cầu của người dùng. Chúng ta sẽ cho nó _thực sự gọi_ hàm sau.

**Chạy và nộp** bài kiểm tra CLI.

### 🇻🇳 Giải thích thêm:

**Khái niệm chính:**
- **Function Declaration** (Khai báo hàm) = Schema mô tả interface của hàm để LLM hiểu cách sử dụng
- **Pattern replication** (Nhân bản mẫu) = Áp dụng cùng cấu trúc từ `schema_get_files_info` cho 3 hàm còn lại
- **Tool expansion** (Mở rộng công cụ) = Thêm nhiều functions vào `available_functions` để LLM có nhiều lựa chọn hơn
- **System prompt update** = Cập nhật "menu" các phép toán mà LLM được phép thực hiện

**Lưu ý quan trọng:**
- Các tham số trong schema chỉ bao gồm những gì LLM cần cung cấp
- Tham số `working_directory` KHÔNG xuất hiện trong schema (bảo mật!)
- LLM chỉ "đề xuất" gọi hàm, không "thực thi" hàm
- Python code của bạn vẫn kiểm soát việc thực thi
