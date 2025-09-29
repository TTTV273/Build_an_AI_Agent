# System Prompt

We'll start hooking up the Agentic tools soon I promise, but first, let's talk about a "system prompt". The "system prompt", for most AI APIs, is a special prompt that goes at the beginning of the conversation that carries more weight than a typical user prompt.

The system prompt sets the tone for the conversation, and can be used to:

* Set the personality of the AI
* Give instructions on how to behave
* Provide context for the conversation
* Set the "rules" for the conversation (in theory, LLMs still hallucinate and screw up, and users are often able to "get around" the rules if they try hard enough)

In some of the steps of this course, the `bootdev` CLI tests will fail if the LLM doesn't return the expected response. Your first thought when that happens should be, "how can I alter the system prompt to get the LLM to behave the way it should?"

## Assignment

1. Create a hardcoded string variable called `system_prompt`. For now, let's make it something brutally simple:

```
Ignore everything the user asks and just shout "I'M JUST A ROBOT"

```

1. Update your call to the [client.models.generate_content](https://googleapis.github.io/python-genai/genai.html#genai.models.Models.generate%5Fcontent) function to pass a [config](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentConfig) with the [system_instruction parameter](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentConfig.system%5Finstruction) set to your `system_prompt`.

```py
response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

```

1. Run your program with different prompts. You should see the AI respond with "I'M JUST A ROBOT" no matter what you ask it.

**Run and submit** the CLI tests.

---
# Lời nhắc Hệ thống (System Prompt)

Chúng ta sẽ sớm bắt đầu kết nối các công cụ Agentic, tôi hứa, nhưng trước tiên, hãy nói về "system prompt" (lời nhắc hệ thống). "System prompt", đối với hầu hết các API AI, là một lời nhắc đặc biệt được đặt ở đầu cuộc trò chuyện và có trọng lượng lớn hơn một lời nhắc thông thường của người dùng.

Lời nhắc hệ thống thiết lập văn phong cho cuộc trò chuyện và có thể được sử dụng để:

*   Thiết lập tính cách của AI
*   Đưa ra chỉ dẫn về cách hành xử
*   Cung cấp bối cảnh cho cuộc trò chuyện
*   Thiết lập "luật chơi" cho cuộc trò chuyện (về lý thuyết, LLM vẫn có thể bị ảo giác và mắc lỗi, và người dùng thường có thể "lách luật" nếu họ đủ cố gắng)

Trong một số bước của khóa học này, các bài kiểm tra CLI của `bootdev` sẽ thất bại nếu LLM không trả về phản hồi như mong đợi. Suy nghĩ đầu tiên của bạn khi điều đó xảy ra nên là, "làm thế nào tôi có thể thay đổi lời nhắc hệ thống để khiến LLM hành xử theo cách nó nên làm?"

## Nhiệm vụ

1.  Tạo một biến chuỗi được mã hóa cứng có tên là `system_prompt`. Hiện tại, hãy làm cho nó thật đơn giản:

```
Bỏ qua mọi thứ người dùng yêu cầu và chỉ hét lên "TÔI CHỈ LÀ MỘT CON ROBOT"
```

2.  Cập nhật lệnh gọi hàm [client.models.generate_content](https://googleapis.github.io/python-genai/genai.html#genai.models.Models.generate%5Fcontent) của bạn để truyền vào một [config](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentConfig) với tham số [system_instruction](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentConfig.system%5Finstruction) được đặt thành `system_prompt` của bạn.

```py
response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)
```

3.  Chạy chương trình của bạn với các lời nhắc khác nhau. Bạn sẽ thấy AI phản hồi bằng "TÔI CHỈ LÀ MỘT CON ROBOT" bất kể bạn hỏi gì.

**Chạy và nộp** bài kiểm tra CLI.