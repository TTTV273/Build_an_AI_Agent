# Build an AI Agent

*Time for Boot.dev to cash in on the **AI hype***.

If you've ever used [Cursor](https://www.cursor.com/en) or [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) as an ["agentic"](https://en.wikipedia.org/wiki/Agentic_AI) AI editor, you'll understand what we're building in this project.

We're **building a toy version of Claude Code** using Google's [free Gemini API](https://ai.google.dev/gemini-api/docs/pricing)! As long as you have an [LLM](https://en.wikipedia.org/wiki/Large_language_model) at your disposal, its actually surprisingly simple to build a (somewhat) effective custom agent.

## What Does the Agent Do?

The program we're building is a CLI tool that:

1. Accepts a coding task (e.g., "strings aren't splitting in my app, pweeze fix >z=I<�=H<�")
2. Chooses from a set of predefined functions to work on the task, for example:
   - Scan the files in a directory
   - Read a file's contents
   - Overwrite a file's contents
   - Execute the python interpreter on a file
3. Repeats step 2 until the task is complete (or it fails miserably, which is possible)

For example, I have a buggy calculator app, so I used my agent to fix the code:

```sh
> uv run main.py "fix my calculator app, its not starting correctly"
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. The output shows the expression and the result in a formatted way.
```

## Prerequisites

- Python 3.10+ installed (see the [bookbot project](https://www.boot.dev/courses/build-bookbot) for help if you don't already have it)
- [uv](https://github.com/astral-sh/uv) project and package manager
- Access to a Unix-like shell (e.g. zsh or bash)

## Learning Goals

The learning goals of this project are:

1. Introduce you to multi-directory Python projects
2. Understand how the AI tools that you'll almost certainly use on the job actually work under the hood
3. Practice your Python and functional programming skills

The goal is *not* to build an LLM from scratch, but to instead use a pre-trained LLM to build an *agent* from scratch.

## Assignment

To get started, make sure you have Python and the [Boot.dev CLI](https://github.com/bootdotdev/bootdev) installed and working.

**Run and submit** the CLI tests.

## Gemini Translation

### **Xây dựng một Agent AI**

*Đã đến lúc Boot.dev tận dụng **cơn sốt AI***.

Nếu bạn đã từng sử dụng [Cursor](https://www.cursor.com/en) hoặc [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) như một trình chỉnh sửa AI có tính "chủ động" ([agentic](https://en.wikipedia.org/wiki/Agentic_AI)), bạn sẽ hiểu chúng ta đang xây dựng gì trong dự án này.

Chúng ta sẽ **xây dựng một phiên bản đồ chơi của Claude Code** bằng cách sử dụng [API Gemini miễn phí](https://ai.google.dev/gemini-api/docs/pricing) của Google! Miễn là bạn có một [LLM](https://en.wikipedia.org/wiki/Large_language_model) trong tay, việc xây dựng một agent tùy chỉnh (phần nào) hiệu quả thực ra lại đơn giản một cách đáng ngạc nhiên.

### **Agent này làm gì?**

Chương trình chúng ta đang xây dựng là một công cụ dòng lệnh (CLI tool) có chức năng:

1. Chấp nhận một nhiệm vụ lập trình (ví dụ: "các chuỗi trong ứng dụng của tôi không tách được, làm ơn sửa giúp >z=I<=H<")
2. Chọn từ một bộ các hàm được định nghĩa trước để thực hiện nhiệm vụ, ví dụ:
   - Quét các tệp trong một thư mục
   - Đọc nội dung của một tệp
   - Ghi đè nội dung của một tệp
   - Thực thi trình thông dịch python trên một tệp
3. Lặp lại bước 2 cho đến khi nhiệm vụ hoàn thành (hoặc thất bại thảm hại, điều này cũng có thể xảy ra)

Ví dụ, tôi có một ứng dụng máy tính bị lỗi, vì vậy tôi đã sử dụng agent của mình để sửa mã:

```sh
> uv run main.py "sửa ứng dụng máy tính của tôi, nó không khởi động đúng cách"
# Đang gọi hàm: get_files_info
# Đang gọi hàm: get_file_content
# Đang gọi hàm: write_file
# Đang gọi hàm: run_python_file
# Đang gọi hàm: write_file
# Đang gọi hàm: run_python_file
# Phản hồi cuối cùng:
# Tuyệt vời! Ứng dụng máy tính bây giờ có vẻ hoạt động chính xác. Kết quả hiển thị biểu thức và đáp án một cách định dạng.
```

### **Điều kiện tiên quyết**

- Đã cài đặt Python 3.10+ (xem dự án [bookbot](https://www.boot.dev/courses/build-bookbot) để được trợ giúp nếu bạn chưa có)
- Trình quản lý gói và dự án [uv](https://github.com/astral-sh/uv)
- Truy cập vào một shell giống Unix (ví dụ: zsh hoặc bash)

### **Mục tiêu học tập**

Các mục tiêu học tập của dự án này là:

1. Giới thiệu cho bạn về các dự án Python có nhiều thư mục
2. Hiểu cách các công cụ AI mà bạn gần như chắc chắn sẽ sử dụng trong công việc thực sự hoạt động "dưới mui xe"
3. Thực hành kỹ năng lập trình Python và lập trình hàm của bạn

Mục tiêu *không phải* là xây dựng một LLM từ đầu, mà thay vào đó là sử dụng một LLM đã được huấn luyện trước để xây dựng một *agent* từ đầu.

### **Nhiệm vụ**

Để bắt đầu, hãy chắc chắn rằng bạn đã cài đặt Python và [Boot.dev CLI](https://github.com/bootdotdev/bootdev) và chúng hoạt động bình thường.

**Chạy và nộp** các bài kiểm tra của CLI.