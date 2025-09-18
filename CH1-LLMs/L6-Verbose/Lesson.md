# CH1-L6: Verbose

## Verbose

As you debug and build your AI agent, you'll probably want to dump a lot more context into the console... but at the same time, we don't want to make the user experience of our CLI tool too noisy...

Let's add an optional command line flag, `--verbose`, that will allow us to toggle "verbose" output on and off. When we want to see more info, we'll just turn that bad boy on.

## Assignment

1. Add a new command line argument, `--verbose`. It should be supplied *after* the prompt if included. For example:

```bash
uv run main.py "What is the meaning of life?" --verbose
```

2. If the `--verbose` flag is included, the console output should include:
   1. The user's prompt: `"User prompt: {user_prompt}"`
   2. The number of prompt tokens on each iteration: `"Prompt tokens: {prompt_tokens}"`
   3. The number of response tokens on each iteration: `"Response tokens: {response_tokens}"`

Otherwise, it should *not* print those things.

**Run and submit** the CLI tests.

## Gemini Translation

### Chế độ Chi tiết

Khi bạn gỡ lỗi và xây dựng agent AI của mình, có thể bạn sẽ muốn xuất nhiều ngữ cảnh hơn ra console... nhưng đồng thời, chúng ta không muốn trải nghiệm người dùng của công cụ CLI (giao diện dòng lệnh) trở nên quá ồn ào...

Hãy thêm một cờ dòng lệnh tùy chọn, `--verbose`, cho phép chúng ta bật và tắt đầu ra "chi tiết". Khi muốn xem thêm thông tin, chúng ta chỉ cần bật tính năng đó lên.

### Nhiệm vụ

1. Thêm một đối số dòng lệnh mới, `--verbose`. Nếu có, nó phải được cung cấp *sau* prompt (lời nhắc). Ví dụ:

   ```bash
   uv run main.py "What is the meaning of life?" --verbose
   ```

2. Nếu cờ `--verbose` được bao gồm, đầu ra của console phải chứa:

   1. Prompt của người dùng: `"User prompt: {user_prompt}"`
   2. Số lượng token của prompt trong mỗi vòng lặp: `"Prompt tokens: {prompt_tokens}"`
   3. Số lượng token của phản hồi trong mỗi vòng lặp: `"Response tokens: {response_tokens}"`

Nếu không, nó *không* được in những thứ đó.

**Chạy và nộp** các bài kiểm tra CLI.

---

Được rồi, nội dung đã được dịch. Giờ chúng ta quay lại câu hỏi ban đầu nhé: Dựa vào cách chúng ta đã làm việc với các đối số dòng lệnh trong các bài trước, bạn nghĩ làm thế nào chúng ta có thể kiểm tra xem người dùng có nhập cờ `--verbose` khi chạy chương trình không?